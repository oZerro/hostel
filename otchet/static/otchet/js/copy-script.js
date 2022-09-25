document.body.onclick = (event) => {
    const elem = event.target;
    var elements = document.querySelectorAll('.copy1')
    var summ_rooms = document.querySelectorAll('.copy2')
    var spendsBoss_zagolovok = document.getElementById('sagol-2').innerHTML
    var spends_Hostel_zagolovok = document.getElementById('sagol-3').innerHTML
    var spendsBoss = document.querySelectorAll('.copy3')
    var itog_spendsBoss = document.querySelectorAll('.copy4')

    var spends_Hoslel = document.querySelectorAll('.copy6')
    var itog_spends_Hostel = document.querySelectorAll('.copy7')
    var text_elem = ""

    var viezds_zagolovok = document.getElementById('sagol-4').innerHTML
    var viezds_3_stolb = document.querySelectorAll('.copy8')
    var viezds_2_stolb = document.querySelectorAll('.copy9')
    var viezds_itog = document.querySelectorAll('.copy10')

    var event_zagolovok = document.getElementById('sagol-5').innerHTML
    var event_2_stolb = document.querySelectorAll('.copy11')

    var event_next_zagolovok = document.getElementById('sagol-6').innerHTML

    var itog_zagolovok = document.getElementById('sagol-7').innerHTML
    var itog_2_stolb = document.querySelectorAll('.copy12')

    for (var i of elements){
        text_elem += i.innerHTML
    }

    room = 0;
    count3 = 0;
    viezds_text = "";
    for (var i of viezds_3_stolb){
        room += 1;
        count3 += 1;
            if (room == 6 && count3 == 1){
                viezds_text += make_two_stolb(viezds_2_stolb);
            }
            else if ( count3 == 1){
                viezds_text += i.innerHTML + " ** ";
            }else if(count3 == 2){
                viezds_text += i.innerHTML + " ** ";
            }else{
                viezds_text += i.innerHTML + '\n';
                count3 = 0;
            }
    }

function make_two_stolb(somth){
    count = 0
    text_elem1 = ""
        for (var i of somth){
            count += 1
            if ( count == 1){
                text_elem1 += i.innerHTML + " - "
            }else{
                text_elem1 += i.innerHTML + '\n'
                count = 0
            }
        }
    return text_elem1.substring(0, text_elem1.length - 1)
}


function make_text_3_stolb(spends){
    count1 = 0
    text_spends = ""
        for (var i of spends){
            count1 += 1
            if ( count1 == 1){
                text_spends += i.innerHTML + " - "
            }else if(count1 == 2){
                text_spends += i.innerHTML + " - "
            }else{
                text_spends += i.innerHTML + '\n'
                count1 = 0
            }
        }

    return text_spends
}



    if (elem.classList.contains('copir')){

        navigator.clipboard.writeText(
        `${text_elem}
         ${make_two_stolb(summ_rooms)}
        ------------------------------------------
        ${spendsBoss_zagolovok}
        ${make_text_3_stolb(spendsBoss)}
        ${itog_spendsBoss[0].innerHTML}  ${itog_spendsBoss[1].innerHTML}
        ------------------------------------------
        ${spends_Hostel_zagolovok}
        ${make_two_stolb(spends_Hoslel)}

        ${itog_spends_Hostel[0].innerHTML}  ${itog_spends_Hostel[1].innerHTML}
        ------------------------------------------
        ${viezds_zagolovok}
        ${viezds_text}
        ${viezds_itog[0].innerHTML}  ${viezds_itog[1].innerHTML}   ${viezds_itog[2].innerHTML}
        ------------------------------------------
        ${event_zagolovok}
        ${make_two_stolb(event_2_stolb)}
        ------------------------------------------
        ${event_next_zagolovok}
        ------------------------------------------
        ${itog_zagolovok}
        ${make_two_stolb(itog_2_stolb)}
        `

        )
    }
}