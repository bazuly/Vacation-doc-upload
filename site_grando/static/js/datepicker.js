$(document).ready(function () {
    console.log("jQuery is working!");
    // Инициализация Datepicker для полей с датами
    $('#id_vacation_date_start').datepicker({
        dateFormat: 'yy-mm-dd'
    });
    $('#id_vacation_date_end').datepicker({
        dateFormat: 'yy-mm-dd'
    });
});
