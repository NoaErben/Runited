$(document).ready(function() {
    // Initialize the calendar on the '#evoCalendar' element
    $('#evoCalendar').evoCalendar({
        theme: 'Royal Navy', // Example theme
        format: 'mm/dd/yyyy',
        titleFormat: 'MM yyyy',
        eventHeaderFormat: 'MM d, yyyy'
    });

    // Optionally, add events to the calendar
    $('#evoCalendar').evoCalendar('addCalendarEvent', [
        {
            id: '09nk7Ts',
            name: "New Year",
            date: "January/1/2024",
            type: "holiday",
            everyYear: true
        }
    ]);
});