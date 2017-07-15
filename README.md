# Metrojobb email hash decoder
Python-converted reverse-engineering on the emails protection function of Metrojobb website.
The service is concealing company email address using JavaScript, was forced to convert it to Python for an asyncronous scraper.

Original JS snippet:

<span class="__cf_email__" data-cfemail="83f5ebe0b2b2c3e8aef1e2f6f7e2adf0e6">[email&#160;protected]</span>
<script data-cfhash='f9e31' type="text/javascript">
/* <![CDATA[ */!function(t,e,r,n,c,a,p){try{t=document.currentScript||function(){for(t=document.getElementsByTagName('script'),e=t.length;e--;)if(t[e].getAttribute('data-cfhash'))return t[e]}();if(t&&(c=t.previousSibling)){p=t.parentNode;if(a=c.getAttribute('data-cfemail')){for(e='',r='0x'+a.substr(0,2)|0,n=2;a.length-n;n+=2)e+='%'+('0'+('0x'+a.substr(n,2)^r).toString(16)).slice(-2);p.replaceChild(document.createTextNode(decodeURIComponent(e)),c)}p.removeChild(t)}}catch(u){}}()/* ]]> 
*/
</script>
