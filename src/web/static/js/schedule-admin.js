var cal = $('#calendar');
var current_event_id = 0;//lazy way of tracking active event being edited
//I suspect this will become something that you're scratching your head over
//while wondering, "why? WHY?"

var games = [];

function updateGamesList() {
    $.getJSON( "/json/games", function( data ) {
        games = data;
        gl = $("#game_select").empty(); //Erase any if we're re-calling
        gl.append($("<option>", {value:-1, text:"Choose a game..."}));
        $.each(games, function (index,g) {
            $("<option>", {
                value: g.pk,
                text: g.name + " (" + g.buzz + " buzz, " + g.plays + " plays)"
            }).attr({
                'data-name': g.name,
                'data-buzz': g.buzz,
                'data-opscomment': g.opscomment,
                'data-plays': g.plays
            }).appendTo(gl);
        });
        $(".game_autocomplete").autocomplete("option", "source",
            $.map(games,function(g,i) { return {label:g.name,value:g.pk}}));
    });
}

function openFormDialog(event, jsev) {
    var _this = jsev.originalEvent;
    console.log(_this);
    current_event_id = event.id;
    update_dialog_info(event)
    $("#dialog_form").dialog({
	autoOpen: true,
	position: {my: 'left', at: 'left', of: _this},
        
	close: function() {
	    $("#dialog_form").dialog("destroy");
	},
    });
}

//fill all the inner form info on the fly in a horrendous fit of JSON abuse
function update_dialog_info(event) {
    console.log(event)
    if (event.id > 0){
        $('#game_select').val(event.gameId); 
    }
    else { 
        $('#game_select').val(-1);
    }
    $('.game_autocomplete').val('');
    $("#event_name").val(event.title);
    $("#dt_start").val(moment(event.start).format('YYYY/MM/DD HH:mm'));
    $("#dt_end").val(moment(event.end).format('YYYY/MM/DD HH:mm'));
    if (event.opscomment) {
        $('#opscommenttext').val(event.opscomment);
    } 
    else {
        $('#opscommenttext').val('');//blank the ops comment
    }


}

//gets all the info in the dialog box in a flagrant abuse of something, I'm sure
function get_dialog_info() {
    var event_data = {}
    event_data = {
        id:     current_event_id,
        name:   $('#event_name').val(),
        game:   $('#game_select').val(),
        start:  moment($('#dt_start').val(),'YYYY/MM/DD HH:mm').format('YYYY-MM-DD HH:mm:ss'),
        end:    moment($('#dt_end').val(),'YYYY/MM/DD HH:mm').format('YYYY-MM-DD HH:mm:ss'),
        opscomment: $('#opscommenttext').val(),
    }
    return event_data
}

function modStart(event){

}

function modEvent(event, delta, revertFunc){
    console.log(event);
    console.log(delta);
    current_event_id = event.eventId;
    update_dialog_info(event);//this is ultra gross why am i even writing this
    console.log(get_dialog_info());
    edit(current_event_id, get_dialog_info(), 'edit');
}


function saveCurrentEvent() {
    console.log('"saved"')

    if ($('#game_select').val() <= 0){
        alert('invalid game')
        console.log('trying to save invalid game id ' +  $('#game_select').val())
        return false
    }
    if ($('#dt_start').val() >= $('#dt_end').val()){
        alert('invalid time(s)');
        console.log('trying to save invalid start/end times ' + $('#dt_start').val() + ' ' + $('#dt_end').val())
        return false
    }

    var form_data = get_dialog_info();
    var action = 'none'
    if (current_event_id <= 0) {
        action = 'new'
    }
    else { 
        action = 'edit'
    }
    edit(current_event_id, form_data, action)
    $("#dialog_form").dialog("destroy");
    return true
}

//get rid of that pesky event(no takebacks)
function deleteCurrentEvent() {
    console.log('deleted: ' + current_event_id)
    $('#calendar').fullCalendar('removeEvents', current_event_id);
    remove(current_event_id);
    $("#dialog_form").dialog("destroy");
}

//open admin page of "current" event(hopefully the one you clicked)
function adminCurrentEvent() {
    console.log('admin-ed: ' + current_event_id)
    window.open("/admin/scheduleentry/edit/?url=%2Fadmin%2Fscheduleentry%2F&id=" + current_event_id)
    $("#dialog_form").dialog("destroy");
}

//set selected game as current in Marathon Info
function currentMarathonInfo() {
    if (current_event_id < 0){
        alert('save entry before setting current game')
        console.log('trying to set marathon schedule with uninitialized schedule')
        return false
    }
    var current_game = get_dialog_info()['game']
    var data = {'action':'current', 'game_id':current_game }
    console.log('setting ' + current_game + ' as current game')
    $.post('/ajax/marathoninfo', data,
        function (success) {
            console.log('AJAX success: server says, "' + success + '"')
            $('#dialog_form').dialog('destroy');
        }
    );
}

//set selected game as next in Marathon Info
function nextMarathonInfo() {
    if (current_event_id < 0){
        alert('save entry before setting next game')
        console.log('trying to set marathon schedule with uninitialized schedule')
        return false
    }
    var current_game = get_dialog_info()['game']
    var data = {'action':'next', 'game_id':current_game }
    console.log('setting ' + current_game + ' as current game')
    $.post('/ajax/marathoninfo', data,
        function (success) {
            console.log('AJAX success: server says, "' + success + '"')
            $('#dialog_form').dialog('destroy');
        }
    );

}
//remove event by id (serverside)
function remove(event_id) {
    var data = {'action':'delete', 'pk': event_id}
    $.post('/ajax/schedulemod', data, 
        function (success) {
            console.log('AJAX success: server says, "' + success + '"')
        }
    );
}

//edit/create event (serverside)
function edit(event_id, data, action) {
    var post_data = {'action':action, 'pk': event_id, 'info':JSON.stringify(data)}
    console.log(post_data)
    $.post('/ajax/schedulemod', post_data,
        function (success) {
            console.log('AJAX success: server says, "' + success + '"')
            $('#calendar').fullCalendar('refetchEvents')
        }
    );
}

//because I have no idea how to push things(TODO w/ free pubnub alternative?)
function force_refresh() {
    console.log('calendar refreshed')
    $('#calendar').fullCalendar('refetchEvents');
}

$(document).ready(function() {
    $( ".game_autocomplete" ).autocomplete({
        select: function( event, ui ) {
            console.log(ui);
            $(this).val(ui.item.label);
            console.log($("#game_select").find("[value="+ui.item.value+"]").prop("selected", true).change());
            return false;
        }
    });

    updateGamesList();
    
    $('#calendar').fullCalendar({
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        height: 600,
        editable: true,
        //defaultDate: '2038-01-19',//for dev purposes only REMOVE REMOVE REMOVE
        selectable: true,
        allDaySlot: false,
        allDayDefault: false,
        defaultView: 'agendaDay',
        timezone: 'America/Los_Angeles',
        theme: true,
        slotDuration: "0:30",
        snapDuration: "0:30",
        defaultTimedEventDuration: "1:00",
        hourLine: true,
        slotEventOverlap: false,
        ignoreTimeZone: false,
        themeButtonIcons: false,
        buttonText: {next: '❯❯', prev: '❮❮'},
        //theme: false,
        themeSystem: 'standard',
	eventResize: modEvent,
	eventDrop: modEvent,
	eventClick: function(event, jsEvent, view) {
            console.log(event);
            console.log('id ' + event.id);
            console.log(jsEvent);
	    openFormDialog(event, jsEvent);
	    //$('#calendar').fullCalendar('rerenderEvents');
	},

        dayClick: function (datetime, jsEv, view) {
            console.log(jsEv)
            current_event_id = -1
            var protoEvent = { //I guess there's no escaping it...
                title:  '',
                id:     -1,
                gameId: -1,
                start:  moment(datetime),
                end:    moment(datetime).add(60, 'm'),

            }
            $('#calendar').fullCalendar('renderEvent', protoEvent)
            console.log(protoEvent)
            openFormDialog(protoEvent, jsEv)
        },

        resources: [
            {title: 'Games', id: 'game'},
            //{title: 'Interviews', id: 'interview'},
            //{title: 'Giveaways', id: 'prize'}
        ],
        eventSources:[
            {
                url: '/json/schedule',
            }
        ],
        eventRender: function (event, eventElement) {
            eventElement.find(".fc-title").append("<div>"+event.opscomment+"</div>");
        }

    });
    //datetimepicker widget in dialogform
    $(".datetimepicker").datetimepicker({
	validateOnBlur:true,
	allowBlank:false,
	onChangeDateTime: function(cdt, $input) {
	    console.log(moment(cdt).format(), $input);
	    //testEvent.update();//change to local update on save only?
	}
    });

});
