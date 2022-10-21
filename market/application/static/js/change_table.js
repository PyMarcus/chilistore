const change_table = () => {
    // monitor window size
    let width = window.screen.width;
    // change class
    if(width < 500){
        let table_id = document.getElementById("tab");
        table_id.classList.remove("table");
        table_id.classList.add("table-responsive");

        let btn1 = document.getElementById("btn1");
        btn1.classList.add("btn-sm");

        let btn1 = document.getElementById("btn2");
        btn1.classList.add("btn-sm");
    }
}