/**
 * Created by BQ0391 on 2017/11/3.
 */


datas = {
    '直辖市':['北京','天津市','上海市','重庆市'],
    '河北省':['石家庄市','张家口市','承德市','秦皇岛市','唐山市','廊坊市','保定市','衡水市','沧州市','邢台市','邯郸市'],
    '山西省':['太原市','朔州市','大同市','长治市','晋城市','忻州市','晋中市','临汾市','吕梁市','运城市'],
    '内蒙古自治区':['呼和浩特市','包头市','乌海市','赤峰市','通辽市','呼伦贝尔市','鄂尔多斯市','乌兰察布市','巴彦淖尔市','兴安盟','锡林多勒盟','阿拉善盟'],
    '江苏省':['南宁市','徐州市','连云港市','宿迁市','淮安市','盐城市','扬州市','秦州市','南通市','镇江市','常州市','无锡市','苏州市'],
    '浙江省':['杭州市','湖州市','嘉兴市','舟山市','宁波市','绍兴市','衢州市','金华市','台州市'],
    '安徽省':['合肥市','宿州市','淮北市','亳州市','阜阳市','蚌埠市','淮南市','滁州市','马鞍山市','芜湖市','安庆市','黄山市','六安市','巢湖市','池州市','宣城市','铜陵市'],
    '福建省':['湖州市','南平市','莆田市','三明市','厦门市','漳州市','龙岩市','宁德市'],
    '江西省':['南昌市','九江市','景德镇市','鹰潭市','新余市','赣州市','上饶市','抚州市','宜春市','吉安市'],
    '山东省':['济南市','聊城市','德州市','东营市','淄博市','潍坊市','烟台市','威海市','日照市','临沂市','枣庄市','济宁市','泰安市','莱芜市','滨州市','菏泽市','青岛市'],
    '四川省':['成都市','广元市','绵阳市','德阳市','南充市','广安市','遂宁市','内江市','乐山市','自贡市','泸州市','宜宾市','巴中市','达州市','资阳市','眉山市','雅安市','阿坝州','甘孜州','凉山州'],
    '贵州省':['贵阳市','六盘水市','遵义市','安顺市','毕节地区','铜仁地区','黔东洲','黔南州','黔西州'],
    '云南省':['昆明市','曲靖市','玉溪市','保山市','昭通市','丽江市','思茅市','临沧市','德宏市','怒江市','迪庆市','大理州','楚雄州','红河州','文山州','西双版纳州'],
    '西藏自治区':['拉萨市','那曲地区','昌都地区','灵芝地区','山南地区','日喀则地区','阿里地区'],
    '辽宁省':['沈阳市','朝阳市',' 阜新市','铁岭市','抚顺市','本溪市','辽阳市','鞍山市','丹东市','大连市','营口市','盘锦市','锦州市','葫芦岛市'],
    '吉林省':['长春市','白城市','松原市','吉林市','四平市','辽源市','通化市','白山市','延边市'],
    '黑龙江省':['哈尔滨市','七台河市','齐齐哈尔市','黑河市','大庆市','鹤岗市','伊春市','佳木斯市','双鸭山市','鸡西市','牡丹江市','绥化市','大兴安岭'],
    '河南省':['郑州市','三门峡市','洛阳市','焦作市','新乡市','鹤壁市','安阳市','濮阳市','开封市','商丘市','许昌市','漯河市','平顶山市','南阳市','周口市','驻马店市'],
    '湖北省':['武汉市','土堰市','襄樊市','荆门市','孝感市','黄冈市','鄂州市','黄石市','咸宁市','宜昌市','枝江市','随州市','恩施州','技江市'],
    '湖南省':['长沙市','张家界市','常德市','益阳市','株洲市','湘潭市','衡阳市','郴州市','永州市','邵阳市','怀化市','娄底市','湘西州'],
    '广东省':['广州市','清远市','韵关市','河源市','梅州市','潮州市','汕头市','揭阳市','汕尾市','惠州市','东莞市','深圳市','珠海市','中山市','江门市','佛山市','肇庆市','云浮市','阳江市','茂名市','湛江市'],
    '广西壮族自治区':['南宁市','桂林市','柳州市','梧州市','贵港市','玉林市','钦州市','北海市','防城港市','崇左市','百色市','河池市','来宾市','贺州市'],
    '海南省':['海口市','三亚市'],
    '陕西省':['西安市','延安市','铜川市','渭南市','咸阳市','宝鸡市','汉中市','榆林市','安康市','商洛市'],
    '甘肃省':['兰州市','嘉谷关市','金昌市','白银市','天水市','武威市','酒泉市','张掖市','庆阳市','平凉市','定西市','陇南市','临夏州','甘南州'],
    '青海省':['西宁市','海东地区','海北州','海南州','黄南州','果洛州','玉树州','海西州'],
    '宁夏回族自治区':['银川市','石嘴山市','固原市','中卫市'],
    '新疆维吾尔自治区':['乌鲁木齐市','克拉玛依市','喀什地区','阿克苏地区','和田地区','吐噜番地区','哈密地区','阿图什市','博乐市','昌吉市','库尔勒市','伊宁市','塔城地区','阿勒泰地区']
}

$(function () {
    st_ipt1 = '<option>--请选择--</option>'
    $.each(datas, function(k){
         st_ipt1 += "<option value="+k+">"+k+"</option>"
    })
    $('#selc_1').html(st_ipt1)
})
$('#selc_1').on('change',function () {
    st_ipt2 = '<option>--请选择--</option>'
    console.log($('#selc_1').val())
    $.each(datas, function (k,v){
        if (k == $('#selc_1').val()) {
            console.log(v.sort())
            $.each(v.sort(), function (key, val) {
                st_ipt2 += "<option value=" + val + ">" + val + "</option>"
            })
        }
    })
    $('#selc_2').html(st_ipt2)
})
$('#selc_2').on('change',function () {

    console.log($('#selc_2').val())
})


//根据文本框输入的汉字自动获取汉字拼音首字母到下拉列表中，支持多音字，需引入库pinying.js
function query(){
    var str = document.getElementById("selectProvince").value.trim();
    if(str == "") return;
    var arrRslt = makePy(str);
    //循环将值到下拉框
    var option = null;
    document.getElementById("select11").innerHTML="";//清空下拉框
    var first = document.getElementById("select11");
    for(var j=0;j<arrRslt.length;j++){
				var obj = document.getElementById("select11");
				obj.add(new Option(arrRslt[j],arrRslt[j]));
    }
}

function arry_lis(data) {
    arry_data = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[],
        'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[],'S':[],'T':[],'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[]}
    $.each(data,function (k) {
        zm = makePy(k)
        switch (zm[0][0]){
            case 'A':
                arry_data['A'].unshift(k);
                break;
            case 'B':
                arry_data['B'].unshift(k);
                break;
            case 'C':
                arry_data['C'].unshift(k);
                break;
            case 'D':
                arry_data['D'].unshift(k);
                break;
            case 'E':
                arry_data['E'].unshift(k);
                break;
            case 'F':
                arry_data['F'].unshift(k);
                break;
            case 'G':
                arry_data['G'].unshift(k);
                break;
            case 'H':
                arry_data['H'].unshift(k);
                break;
            case 'I':
                arry_data['I'].unshift(k);
                break;
            case 'J':
                arry_data['J'].unshift(k);
                break;
            case 'K':
                arry_data['K'].unshift(k);
                break;
            case 'L':
                arry_data['L'].unshift(k);
                break;
            case 'M':
                arry_data['M'].unshift(k);
                break;
            case 'N':
                arry_data['N'].unshift(k);
                break;
            case 'O':
                arry_data['O'].unshift(k);
                break;
            case 'P':
                arry_data['P'].unshift(k);
                break;
            case 'Q':
                arry_data['Q'].unshift(k);
                break;
            case 'R':
                arry_data['R'].unshift(k);
                break;
            case 'S':
                arry_data['S'].unshift(k);
                break;
            case 'T':
                arry_data['T'].unshift(k);
                break;
            case 'U':
                arry_data['U'].unshift(k);
                break;
            case 'V':
                arry_data['V'].unshift(k);
                break;
            case 'W':
                arry_data['W'].unshift(k);
                break;
            case 'X':
                arry_data['X'].unshift(k);
                break;
            case 'Y':
                arry_data['Y'].unshift(k);
                break;
            case 'Z':
                arry_data['Z'].unshift(k);
                break;
            default:
                break;
        }
    })
    return arry_data
}

function arry_li(data) {
    arry_data = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[],
        'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[],'S':[],'T':[],'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[]}
    $.each(data,function (v,k) {
        zm = makePy(k)
        switch (zm[0][0]){
            case 'A':
                arry_data['A'].unshift(k);
                break;
            case 'B':
                arry_data['B'].unshift(k);
                break;
            case 'C':
                arry_data['C'].unshift(k);
                break;
            case 'D':
                arry_data['D'].unshift(k);
                break;
            case 'E':
                arry_data['E'].unshift(k);
                break;
            case 'F':
                arry_data['F'].unshift(k);
                break;
            case 'G':
                arry_data['G'].unshift(k);
                break;
            case 'H':
                arry_data['H'].unshift(k);
                break;
            case 'I':
                arry_data['I'].unshift(k);
                break;
            case 'J':
                arry_data['J'].unshift(k);
                break;
            case 'K':
                arry_data['K'].unshift(k);
                break;
            case 'L':
                arry_data['L'].unshift(k);
                break;
            case 'M':
                arry_data['M'].unshift(k);
                break;
            case 'N':
                arry_data['N'].unshift(k);
                break;
            case 'O':
                arry_data['O'].unshift(k);
                break;
            case 'P':
                arry_data['P'].unshift(k);
                break;
            case 'Q':
                arry_data['Q'].unshift(k);
                break;
            case 'R':
                arry_data['R'].unshift(k);
                break;
            case 'S':
                arry_data['S'].unshift(k);
                break;
            case 'T':
                arry_data['T'].unshift(k);
                break;
            case 'U':
                arry_data['U'].unshift(k);
                break;
            case 'V':
                arry_data['V'].unshift(k);
                break;
            case 'W':
                arry_data['W'].unshift(k);
                break;
            case 'X':
                arry_data['X'].unshift(k);
                break;
            case 'Y':
                arry_data['Y'].unshift(k);
                break;
            case 'Z':
                arry_data['Z'].unshift(k);
                break;
            default:
                break;
        }
    })
    return arry_data
}

function pinjie_sf() {
    str_html = ''
    $.each(arry_lis(datas),function(k,v){
        count = 0
        if(v!=''){
            str_html += "<li><b>"+k+"</b>"
            if (v.length>4){
                $.each(v,function (key,val) {
                    if(count >4){
                        str_html +='<li><a href="javascript:void(0);">'+val+'</a>'
                    }
                    if(count == v.length){
                        str_html +='</li>'
                    }
                    str_html += '<a href="javascript:void(0);">'+val+'</a>'
                    count +=1
                })
            }else{
                $.each(v,function (key,val) {
                    str_html += '<a href="javascript:void(0);">'+val+'</a>'
                })
            }
            str_html +='</li>'
        }
    })
    $('#allProvince').html(str_html)
}

function pinjie(data) {
    str_html = ''
    $.each(arry_li(data),function(k,v){
        count = 0
        if(v!=''){
            str_html += "<li><b>"+k+"</b>"
            if (v.length>4){
                $.each(v,function (key,val) {
                    if(count >4){
                        str_html +='<li><a href="javascript:void(0);">'+val+'</a>'
                    }
                    if(count == v.length){
                        str_html +='</li>'
                    }
                    str_html += '<a href="javascript:void(0);">'+val+'</a>'
                    count +=1
                })
            }else{
                $.each(v,function (key,val) {
                    str_html += '<a href="javascript:void(0);">'+val+'</a>'
                })
            }
            str_html +='</li>'
        }
    })
    return str_html
}

$(function () {
    $("#allProvince").delegate('a', 'click', function (evt) {
         evt.stopPropagation()
         $('#selectProvince').val($(this).html())
         $('#allProvince').hide()
         $('#allProvince').html('')
         $('#allProvince2').html(pinjie(datas[$(this).html()]))
         zhanshi()
    })
    $("#allProvince2").delegate('a', 'click', function (evt) {
         evt.stopPropagation()
         val = $(this).html()
         $('#allProvince2').hide()
         $('#allProvince2').html('')
         $('#selectProvince').val($('#selectProvince').val()+'-'+val)
    })
})

$('#selectProvince').on('click', function (e) {
     $('#allProvince').html(pinjie_sf())
     $('#allProvince2').html('')
     e.stopPropagation()
    $('#allProvince').show()
})

function zhanshi() {
    $('#allProvince2').show()
}


