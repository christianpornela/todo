$(document).ready(function(){

    var url = 'http://127.0.0.1:8000/api/v1/todo';
 
    // button click event listener
    $('#btn').click(function(){
        // AJAX request
        $.ajax({
            url: url,
            type: "GET",
            success: function(result){
                // print out the data
                var stringifiedData = JSON.stringify(result);
                var ourData = JSON.parse(stringifiedData);
                // render the data as HTML
                renderHTML(ourData);
            },
            error: function(xhr, status, error){
                // print out the error
                console.log('Error: ' + xhr.responseText);
            }
        })
    })
 
    function renderHTML(data) {
        var htmlString = "";
 
        for(i = data.length-1; i > -1; i--){
			
			var MyTable =  
                document.getElementById("todo"); 
            
            // insert new row. 
            var NewRow = MyTable.insertRow(1); 
            var Newcell1 = NewRow.insertCell(0); 
            var Newcell2 = NewRow.insertCell(1); 
			var Newcell3 = NewRow.insertCell(2); 
			var Newcell4 = NewRow.insertCell(3); 
			var Newcell5 = NewRow.insertCell(4);
			var Newcell6 = NewRow.insertCell(5); 
			var Newcell7 = NewRow.insertCell(6); 
            Newcell1.innerHTML = "<button type='button' id='row' class='btn'/>Select"; 
            Newcell2.innerHTML = data[i].title; 
			Newcell3.innerHTML = data[i].notes; 
			Newcell4.innerHTML = data[i].due_date; 
			var categorytext=data[i].category
			switch(categorytext){
				case 1:
					categorytext="Groceries";
					break;
				case 2:
					categorytext="Movies to watch";
					break;
				case 3:
					categorytext="Travel";
					break;
				case 4:
					categorytext="Work";
					break;
				case 5:
					categorytext="Family";
					break;
				case 6:
					categorytext="Private";
					break;
			}
			Newcell5.innerHTML = categorytext; 
			var prioritytext=data[i].priority
			switch(prioritytext){
				case 1:
					prioritytext="Low";
					break;
				case 2:
					prioritytext="Medium";
					break;
				case 3:
					prioritytext="High";
					break;
			}
			Newcell6.innerHTML = prioritytext; 
			if	(data[i].isStarred){
				Newcell7.innerHTML ="<i class='fa fa-star'></i>"; 
			}
			else{
				Newcell7.innerHTML ="<i class='fa fa-star-o'></i>"; 
			}
			$('#row').click(function() {
				var $item = $(this).closest("tr"),
				 $tds = $item.find("td:nth-child(2)").text();
				document.getElementById("name").value=$tds;
			})

        }

    }
 
})


 