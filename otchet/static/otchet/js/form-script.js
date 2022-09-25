console.log("arrwe");

var append_but_peopl = document.getElementById("append_but_peopl");

function add_peop(){
    var add_pep_form = document.getElementById("add_pep_form");
    add_pep_form.style = "display:flex; opacity:1";
}

function close_add_peopl(){
    var add_pep_form = document.getElementById("add_pep_form");
    add_pep_form.style = "display:none";
}
//-------------------------------------------------------------------------------

function add_pay(){
    var add_pay_form = document.getElementById("add_pay_form");
    add_pay_form.style = "display:flex; opacity:1";
}

function close_add_pay(){
    var add_pay_form = document.getElementById("add_pay_form");
    add_pay_form.style = "display:none";
}

//-------------------------------------------------------------------------------

function add_spend_admin(){
    var add_spend_admin_form = document.getElementById("add_spend_admin_form");
    add_spend_admin_form.style = "display:flex; opacity:1";
}

function close_add_spend_admin(){
    var add_spend_admin_form = document.getElementById("add_spend_admin_form");
    add_spend_admin_form.style = "display:none";
}

//-------------------------------------------------------------------------------

function add_spend_hostel(){
    var add_spend_hostel_form = document.getElementById("add_spend_hostel_form");
    add_spend_hostel_form.style = "display:flex; opacity:1";
}

function close_add_spend_hostel(){
    var add_spend_hostel_form = document.getElementById("add_spend_hostel_form");
    add_spend_hostel_form.style = "display:none";
}

//-------------------------------------------------------------------------------

function add_spend_boss(){
    var add_spend_boss_form = document.getElementById("add_spend_boss_form");
    add_spend_boss_form.style = "display:flex; opacity:1";
}

function close_add_spend_boss(){
    var add_spend_boss_form = document.getElementById("add_spend_boss_form");
    add_spend_boss_form.style = "display:none";
}

//-------------------------------------------------------------------------------

function add_event(){
    var add_event_form = document.getElementById("add_event_form");
    add_event_form.style = "display:flex; opacity:1";
}

function close_add_event(){
    var add_event_form = document.getElementById("add_event_form");
    add_event_form.style = "display:none";
}

//-------------------------------------------------------------------------------

function add_ref(){
    var add_ref_form = document.getElementById("add_ref_form");
    add_ref_form.style = "display:flex; opacity:1";
}

function close_add_ref(){
    var add_ref_form = document.getElementById("add_ref_form");
    add_ref_form.style = "display:none";
}

//-------------------------------------------------------------------------------

function add_ref_pay(){
    var pay_ref_checkbox = document.getElementById("pay_ref");
    var ul_pay_ref = document.getElementById("ul_pay_ref");
    if (pay_ref_checkbox.checked){
        ul_pay_ref.style = "height: 0;";
        ul_pay_ref.style = "padding: 0px 20px;";
    } else{
        ul_pay_ref.style = "width: 120%; height: 145px; padding: 20px; left: -16px;";


    }

}


//-------------------------------------------------------------------------------

function depart_peop(){
    var depart_form = document.getElementById("depart_form");
    depart_form.style = "display:flex; opacity:1";
}

function close_depart_peopl(){
    var depart_form = document.getElementById("depart_form");
    depart_form.style = "display:none";
}

//-------------------------------------------------------------------------------

function update_pay_form(){
    var update_pay_form = document.getElementById("update_pay_form");
    update_pay_form.style = "display:flex; opacity:1";
}

function close_update_pay_form(){
    var update_pay_form = document.getElementById("update_pay_form");
    update_pay_form.style = "display:none";
}


//-------------------------------------------------------------------------------

function open_media_menu(){
    var media_menu = document.getElementById("menu-media");
    media_menu.style = "right: 0;";
}

function close_media_menu(){
    var media_menu = document.getElementById("menu-media");
    media_menu.style = "right: -108%;";
}



