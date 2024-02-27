<script>
    function getQueryString(name) {
        let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
        let r = window.location.search.substr(1).match(reg);
        if (r != null) {
            return decodeURIComponent(r[2]);
        };
        return null;
    }

    var name = getQueryString("name");
    setTimeout("console.log('" + name + "')", 100);
</script>

<!-- 
payload: 

')-alert(1)//

减法：   减之前需要执行这个payload,然后才会带入，所以触发alert函数 -->