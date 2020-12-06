function convertHTML(str) {
   const stringMap = {
       '&': '&amp;',
       '<': '&lt;',
       '>': '&gt;',
       '"': '&quot;',
       "'": '&apos;'
   }
   Object.keys(stringMap).forEach( key => {
       const regex =  new RegExp(key, 'g');
       str = str.replace(regex,stringMap[key]);
   })
  return str;
}

convertHTML("Dolce & Gabbana"); //should return "Dolce &amp; Gabbana";
convertHTML("Hamburgers < Pizza < Tacos"); //should return "Hamburgers &lt; Pizza &lt; Tacos";
convertHTML("Sixty > twelve"); //should return "Sixty &gt; twelve"
convertHTML('Stuff in "quotation marks"'); //should return "Stuff in &quot;quotation marks&quot;"
convertHTML("Schindler's List") //should return "Schindler&apos;s List"
convertHTML("<>"); //should return "&lt;&gt;"
convertHTML("abc") //should return "abc"
