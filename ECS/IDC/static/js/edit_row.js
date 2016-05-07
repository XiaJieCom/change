
$(function(){
    BindSingleCheck('#edit_mode', '#tb1');
});

function BindSingleCheck(mode, tb){

    $(tb).find(':checkbox').bind('click', function(){
        var $tr = $(this).parent().parent();
        if($(mode).hasClass('editing')){
            if($(this).prop('checked')){
                RowIntoEdit($tr);
            }else{
                RowOutEdit($tr);
            }
        }
    });
}

function CreateSelect(attrs,csses,option_dict,item_key,item_value,current_val){
    var sel= document.createElement('select');
    $.each(attrs,function(k,v){
        $(sel).attr(k,v);
    });
    $.each(csses,function(k,v){
        $(sel).css(k,v);
    });
    $.each(option_dict,function(k,v){
        var opt1=document.createElement('option');
        var sel_text = v[item_value];
        var sel_value = v[item_key];

        if(sel_value==current_val){
            $(opt1).text(sel_text).attr('value', sel_value).attr('text', sel_text).attr('selected',true).appendTo($(sel));
        }else{
            $(opt1).text(sel_text).attr('value', sel_value).attr('text', sel_text).appendTo($(sel));
        }
    });
    return sel;
}

STATUS = [
    {'id': 1, 'value': "在线"},
    {'id': 2, 'value': "下线"}
];

BUSINESS = [
    {'id': 1, 'value': "车上会"},
    {'id': 2, 'value': "二手车"}
];

function RowIntoEdit(_tr){
	// tr = 选择器，当前行
    _tr.children().each(function(){
		// $(this)，当前循环元素，当前td
        if($(this).attr('edit') == "true"){
            if($(this).attr('edit-type') == "select"){
				// 在线，对应的value
                var select_val = $(this).attr('sel-val');
				// global_key全局变量的变量名
                var global_key = $(this).attr('global-key');
				// 创建select标签，并且，select标签选中当前的之
				/*
				<select onchange = "MultiSelect(this)">
					<option value='1' selected='selected'> 在线</option>
					<option value='2'> 下线</option>
				</select>
				*/
                var selelct_tag = CreateSelect({"onchange": "MultiSelect(this);"}, {}, window[global_key], 'id', 'value', select_val);
                $(this).html(selelct_tag);
            }else{
                var orgin_value = $(this).text();
                var temp = "<input value='"+ orgin_value+"' />";
                $(this).html(temp);
            }

        }
    });
}

function RowOutEdit($tr){
    $tr.children().each(function(){
        if($(this).attr('edit') == "true"){
            if($(this).attr('edit-type') == "select"){
                var new_val = $(this).children(':first').val();
                var new_text = $(this).children(':first').find("option[value='"+new_val+"']").text();
                $(this).attr('sel-val', new_val);
                $(this).text(new_text);
            }else{
                var orgin_value = $(this).children().first().val();
                $(this).text(orgin_value);
            }

        }
    });
}

function CheckAll(mode, tb){
	// mode = "#edit_mode"   
	// tb = "#tb1"
    if($(mode).hasClass('editing')){
		// 选中所有的checkbox，并将所有行处理成进入编辑模式
        // $(tb).children() 所有的tr
		$(tb).children().each(function(){
			// 每一个tr
            var tr = $(this);
			// 每个tr中的checkbox
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){

            }else{
				// 未进入编辑模式的行
                check_box.prop('checked',true);
				
				// 让一行进入编辑模式，参数：选择器当前行
                RowIntoEdit(tr);
            }
        });

    }else{
		// 选中所有的checkbox
        $(tb).find(':checkbox').prop('checked', true);
    }
}

function CheckReverse(mode, tb){

    if($(mode).hasClass('editing')){

        $(tb).children().each(function(){
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                check_box.prop('checked',false);
                RowOutEdit(tr);
            }else{
                check_box.prop('checked',true);
                RowIntoEdit(tr);
            }
        });


    }else{
        //
        $(tb).children().each(function(){
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                check_box.prop('checked',false);
            }else{
                check_box.prop('checked',true);
            }
        });
    }
}

function CheckCancel(mode, tb){
    if($(mode).hasClass('editing')){
        $(tb).children().each(function(){
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                check_box.prop('checked',false);
				// 当前行推出编辑模式
                RowOutEdit(tr);

            }else{

            }
        });

    }else{
        $(tb).find(':checkbox').prop('checked', false);
    }
}

function EditMode(ths, tb){
    if($(ths).hasClass('editing')){
        $(ths).removeClass('editing');
        $(tb).children().each(function(){
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                RowOutEdit(tr);
            }else{

            }
        });

    }else{

        $(ths).addClass('editing');
        $(tb).children().each(function(){
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                RowIntoEdit(tr);
            }else{

            }
        });

    }
}



