/**
 * Created by jack on 16/6/1.
 */
function Func_hide(ths){
    $(ths).next().removeClass('hide');
    $(ths).parent().siblings().find('.menu_body').addClass('hide');
}

function AllBind(ths){
    $("input[type='checkbox']").attr("checked",true);
}
function SelectAll(){
//            checked 设置默认是否选中
//            先找到所有table下的chekcbox,然后使用prop给checked设置ture 或者false
    $('table :checkbox').prop('checked',true);
}
function OtherBind(ths){
    $("input[type='checkbox']").each(function (){
        this.checked = !this.checked;
    })
}
function NoBind(ths){
    $("input[type='checkbox']").removeAttr("checked");
}
function FuncRemove(ths){
    $("#divHide").removeClass('hide');

}
function showdiv() {
    document.getElementById("bg").style.display ="block";
    document.getElementById("show").style.display ="block";
}
function hidediv() {
    document.getElementById("bg").style.display ='none';
    document.getElementById("show").style.display ='none';
}
