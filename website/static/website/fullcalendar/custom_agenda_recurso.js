
document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'interaction', 'resourceTimeline', 'timeGrid' ],
    selectable: true,
    defaultView: 'resourceTimelineWeek',
	/*defaultDate: str_data,
    editable: false,
    navLinks: true, // can click day/week names to navigate views
    eventLimit: true, // allow "more" link when too many events*/
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'resourceTimelineWeek,timeGridDay'
    },
    resources: [
      { id: 'a', title: 'Room A' },
      { id: 'b', title: 'Room B' },
      { id: 'c', title: 'Room C' }
    ],
    dateClick: function(info) {
      alert('clicked ' + info.dateStr + ' on resource ' + info.resource.id);
    },
  });

  calendar.render();
});    
