$(document).ready(function() {
    $('#calendar').fullCalendar({
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
            {
              name: 'Games',
              id: 'game',
              clickOffset: 0
            },
            {
              name: 'Interviews',
              id: 'interview',
              clickOffset: 1
            },
            {
              name: 'Giveaways',
              id: 'raffle',
              clickOffset: 2
            }
        ]
        // eventSources:[
        //     {
        //         url: '/ajax/schedule/',
        //         success: function(data, status, jqXHR) {data.forEach(convertServerEvent);}
        //     }
        // ]
    })
});
