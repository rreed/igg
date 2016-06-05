$(document).ready(function() {
    $('#calendar').fullCalendar({
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        height: 600,
        editable: false,
        //selectable: true,
        allDaySlot: false,
        allDayDefault: false,
        defaultView: 'agendaDay',
        timezone: 'America/Los_Angeles',
        theme: true,
        slotDuration: "0:30",
        snapDuration: "0:10",
        defaultTimedEventDuration: "0:30",
        hourLine: true,
        slotEventOverlap: false,
        ignoreTimeZone: false,
        themeButtonIcons: false,
        buttonText: {next: '❯❯', prev: '❮❮'},
        resources: [
            {title: 'Games', id: 'game'},
            {title: 'Interviews', id: 'interview'},
            {title: 'Giveaways', id: 'prize'}
        ],
        eventSources:[
            {
                url: '/json/schedule',
                success: function(data, status, jqXHR) {data.forEach(convertServerEvent);}
            }
        ]
    })
});

function convertServerEvent(e) {
    e.changed = false;
}
