$('button').on('click',function(){
    let tasa = parseFloat($('#tasa').val())  ;
    let monto=  parseFloat($('#monto').val());
    let plazo=  parseFloat($('#plazo').val());
    let tasaMensual= tasa/100/12;
    let cuota =(monto * tasaMensual) / (1 - Math.pow(1+tasaMensual, -plazo));
    $('#cuota').text(cuota);
    $('#total').text(cuota*plazo);
})