def web_generation(web_json,publications):
  web = ""
  web_head = """<!DOCTYPE html>
  <html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Influential Cybersecurity Researchers and Their Representative Publications</title>
    <script src="./script/jquery.min.js.download"></script>
    <script src="./script/stupidtable.js.download"></script>
    <script>
      $(function(){
          var table = $("table").stupidtable();
          table.bind('aftertablesort', function (event, data) {
            var table = $(this)[0],
            rows = table.getElementsByTagName('tr');
            for(var i = 0, len = rows[1].children.length; i < len; i++){
              rows[1].children[i].textContent = rows[1].children[i].textContent.replace('\\u25B2','')
              rows[1].children[i].textContent = rows[1].children[i].textContent.replace('\\u25BC','')
            }
            if(data.direction  == "asc")
              rows[1].children[data.column].textContent += "\\u25B2"
            else
              rows[1].children[data.column].textContent += "\\u25BC"
            var prev_v = -1,prev_r;
            for (var i = 0, len = rows.length-2; i < len; i++){
              var r = i+1
              if(data.direction == "asc")
                r = rows.length-2-(i)
              var v = rows[i+2].children[data.column].textContent;
              if(prev_v != v){
                rows[i+2].children[0].textContent = "" + r;
                prev_r = r;
              }
              else
                rows[i+2].children[0].textContent = "" + prev_r;
              prev_v = v;
            }
          });
      });
    </script>
    
    <script>
    function display(clickable,cf,element,name){
      """
  web_head += "var publications ="
  web_head += str(publications)
  web_head +=		"""
      var container = document.getElementById("containerTab")
      var content = "";
      var rect = clickable.getBoundingClientRect();
      if(container.style.display == "block"){
        //console.log("current state: block");
        container.style.display ="none";
      } else{
        //console.log("current state: none");
        container.style.display ="block";
      }
      content += "<span onclick=\\"this.parentElement.style.display=\\'none\\'\\" class=\\"closebtn\\">&times;<\\/span>";
          content += "<h2>" + name; 
      if(cf == "All" || cf == "Tier 1")
        content += "'s publication in " + cf + " conference<\\/h2>";
      else
        content += "'s " + cf + " publication<\\/h2>";
      for (i = 0; i < element.length; i++){
      content += "<p>"+ (i+1) + ".";
        for(j = 0; j < publications[element[i]].author.length; j++){
          content += publications[element[i]].author[j] + ", ";
        }
      content += "\\n<i>";
      content += publications[element[i]].name + "<\\/i>; Published Conference: " +publications[element[i]].year
      + ' ' + publications[element[i]].conference+ ", [cited by:"  
        + ((publications[element[i]].citation > 0) ? (publications[element[i]].citation) : "N/A") + "]\\n";
        content += "<\\/p>\\n";
      }
      $("#containerTab").html(content);
      $("#containerTab").css({'top' : (rect.top+20+window.scrollY) + 'px'});
    }
    </script>  
    
    <style type="text/css">
      table {
        border-collapse: collapse;
      }
      th, td {
        padding: 5px 10px;
        border: 1px solid #999;
      }
      th {
        background-color: #eee;
      }
      th[data-sort]{
        cursor:pointer;
      }
    
    .containerTab {
      padding: 10px;
      color: white;
      height: 500px;
      left: 20%;
      width: 60%;
      position:absolute;
          overflow: auto;
    }
    .closebtn {
      float: right;
      color: white;
      font-size: 35px;
      cursor: pointer;
    }
    
    </style>
    
  </head>

  <body>

    <h1>Influential Cybersecurity Researchers and Their Representative Publications</h1>

    <p>Sorting function achieve with library Stupid Jquery table sort</p>

    <table>
      <thead>
        <tr>
          <th colspan="2"></th>
          <th colspan="3">Total</th>
          <th colspan="3">Tier 1 Only</th>
      <th colspan="2">Top 5 Publication</th>
      <th colspan="2">Top 10 Publication</th>
          <th ></th>
          <th ></th>
        </tr>
        <tr>
          <th>Ranking</th>
          <th>Scholar</th>
          <th data-sort="int" data-sort-default="desc">Publication</th>
          <th data-sort="int" data-sort-default="desc">Citation\u25BC</th>
          <th data-sort="int" data-sort-default="desc">Citation Per Publication</th>
          <th data-sort="int" data-sort-default="desc">Publication</th>
          <th data-sort="int" data-sort-default="desc">Citation</th>
          <th data-sort="int" data-sort-default="desc">Citation Per Publication</th>
          <th data-sort="int" data-sort-default="desc">Citation</th>
          <th data-sort="int" data-sort-default="desc">Citation Per Publication</th>
          <th data-sort="int" data-sort-default="desc">Citation</th>
          <th data-sort="int" data-sort-default="desc">Citation Per Publication</th>
          <th data-sort="string" >Last Affilation</th>
      <th>Google Scholar link</th>
        </tr>
      </thead>
      <tbody>
  """

  web_tail = """  <div id ="containerTab" class="containerTab" style="display:none;background:green">
  </div>
  </body></html>"""

  web += web_head
  table = ""
  for i,author in enumerate(web_json):
  #for i in range(20):
      #i += 40
      #author = authors[i]
      table += "<tr>"
      #name
      table += "<td>" + str(i+1) + "</td>"
      table += "<td>" + author["name"] + "</td>"
      table += """<td onclick = "display(this,'All',""" + str(author["all"]) + ",\'" + author["name"] + """')"><u>""" + str(len(author["all"])) + """</u></td>"""
      table += """<td>""" + str(author["total_citation"]) + "</td>"
      table += """<td>""" + str(int(author["total_avg"])) + "</td>"
      table += """<td onclick = "display(this,'Tier 1',""" + str(author["tier_1"]) + ",\'" + author["name"] + """')"><u>""" + str(len(author["tier_1"])) + """</u></td>"""
      table += """<td>""" + str(author["tier_1_citation"]) + "</td>"
      table += """<td>""" + str(int(author["tier_1_avg"])) + "</td>"
      table += """<td onclick = "display(this,'Top 5',""" + str(author["all"][:5]) + ",\'" + author["name"] + """')"><u>""" + str(author["top_5"]) + """</u></td>"""
      table += """<td>""" + str(int(author["top_5_avg"])) + "</td>"
      max_n = min(len(author["all"]),10)
      table += """<td onclick = "display(this,'Top 10',""" + str(author["all"][:max_n]) + ",\'" + author["name"] + """')"><u>""" + str(author["top_10"]) + """</u></td>"""
      table += """<td>""" + str(int(author["top_10_avg"])) + "</td>"
      table += """<td>""" + author["affiliation"] + """</td>"""
      if "gs_link" in author:
        if author["gs_link"]!="":
          table += """<td><a href=\"""" + author["gs_link"] + """\"><u style = "color:blue">G</u></a></td>"""
        else:      
          table += """<td></td>"""
      else:
        table += """<td></td>"""
      table += """</tr>\n"""
  web += table
  web+= """
        </tbody>
    </table>
  """

  web += web_tail

  f = open( 'website/test.html', 'w',encoding='utf-8' )
  f.write( web )
  f.close()
    