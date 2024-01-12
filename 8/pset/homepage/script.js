document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#show_fiftyville').addEventListener('click', function(event)
    {
        document.getElementById("solution_fiftyville").setAttribute('visibility ', 'visible');
        event.preventDefault();
    });
});

