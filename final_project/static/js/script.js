function select_subject(option) {
    if (option == "")
    {
        return;
    }

    if (option == "add_subject")
    {
        document.getElementById("display_calculator").innerHTML = ""; // clear calculator template if add subject clicked, so they never both get displayed
        new_subject_form();
    }
    else
    {
        document.getElementById("add_subject_input_field").innerHTML = ""; // clear add subject flied if previously clicked and the changed your mind
        calculator_template();
    }
}

function new_subject_form()
{
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function() {
        if (ajax.readyState == 4 && ajax.status == 200)
        {
            document.getElementById("add_subject_input_field").innerHTML = ajax.responseText;
        }
    };
    ajax.open("GET", "static/ajax/add_subject.html", false);
    ajax.send();
}


function calculator_template()
{
    var ajax = new XMLHttpRequest();
    ajax.onreadystatechange = function() {
        if (ajax.readyState == 4 && ajax.status == 200)
        {
            document.getElementById("display_calculator").innerHTML = ajax.responseText;
        }
    };
    ajax.open("GET", "static/ajax/calculator_template.html", false);
    ajax.send();
}

function calculate_grade(id)
{
    let temp = 0;


    temp = document.getElementById("written_percentage");
    temp = temp.value;
    let written_percentage = Number(temp);



    temp = document.getElementById("oral_percentage");
    temp = temp.value;
    let oral_percentage = Number(temp);


    temp = document.getElementById("written_grade");
    temp = temp.value;
    let written_grade = Number(temp);


    temp = document.getElementById("oral_grade");
    temp = temp.value;
    let oral_grade = Number(temp);


    let calculated_grade = ((written_percentage * written_grade) + (oral_percentage * oral_grade)) / (written_percentage + oral_percentage);
    calculated_grade = (Math.round(calculated_grade * 100) / 100).toFixed(2);
    if (calculated_grade >= 1 && calculated_grade <= 6)
    {
        document.getElementById("calculated_grade_input").value = calculated_grade;
        document.getElementById("calculated_grade_paragraph").innerText = calculated_grade;
    }
    else
    {
        document.getElementById("calculated_grade_input").value = "";
        document.getElementById("calculated_grade_paragraph").innerText = "Waiting for values";
    }
}
