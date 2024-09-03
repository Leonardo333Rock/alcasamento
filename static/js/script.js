presentes = [...document.querySelectorAll('.card')]


 presentes.map((e)=>{
    qt = e.children[1].children[3].children[0].innerHTML
    
    if(qt == 0){
        e.children[1].children[3].innerHTML = "Indisponivel"
        e.children[1].children[3].setAttribute('class','indisponivel')
        e.children[1].children[2].remove()

        let p = document.createElement('p')
        p.setAttribute('class', 'presenteado')
        // p.innerHTML='Presenteado por: Neuriane e Reginaldo'
        e.children[1].appendChild(p)
     }
 })