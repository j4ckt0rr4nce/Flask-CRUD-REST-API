$( document ).ready(function() {

    $('#submit-file').on("click",function(e){
		e.preventDefault();
		$('#files').parse({
			config: {
				delimiter: ",",
                skipEmptyLines: true,
				complete: function(results, file) {
                    const data = results.data
                    for (i in data){
                        fetch("http://localhost:5000/item", {
                            method: 'POST',
                            body: JSON.stringify({
                                id:parseInt(data[i][0]),
                                internal_identifier:data[i][1],
                                price:parseFloat(data[i][2]),
                                description:data[i][3],
                                order_id:parseInt(data[i][4]),
                            }),
                            headers:{
                                'Content-type': 'application/json; charset=UTF-8',
                            }
                        })
                        .then(function(response){ 
                            return response.json()})
                        .then(function(data){
                            console.log(data)
                        })
                        .catch(error => console.error('Error:', error))
                    } 
                },
			},
			before: function(file, inputElem)
			{
				//console.log("Parsing file...", file);
			},
			error: function(err, file)
			{
				console.log("ERROR:", err, file);
			},
			complete: function()
			{
				//console.log("Done with all files");
			}
		})
    })
	
    const personForm = document.getElementById('person_form')
 
    personForm.addEventListener('submit', function(e){

        const id = document.querySelector('input[name="p_id"]').value
        const phone = document.querySelector('input[name="p_phone_number"]').value
        const email = document.querySelector('input[name="p_email_address"]').value
        const fname = document.querySelector('input[name="p_first_name"]').value
        const lname = document.querySelector('input[name="p_last_name"]').value
        const birth = document.querySelector('input[name="p_date_of_birth"]').value
        const updateId = document.querySelector('input[name="p_put_id"]').value

        e.preventDefault()
        if (updateId == "" ){
            fetch("http://localhost:5000/person", {
                method: 'POST',
                body: JSON.stringify({
                    id:parseInt(id),
                    phone_number:parseInt(phone),
                    email_address:email,
                    customer_type:"person",
                    first_name:fname,
                    last_name:lname,
                    date_of_birth:birth,
                }),
                headers:{
                    'Content-type': 'application/json; charset=UTF-8',
                }
            })
            .then(function(response){ 
                return response.json()})
            .then(function(data){
                console.log(data)
                pBuildList()
            })
            .catch(error => console.error('Error:', error))           
        } else{
            const customer_id = parseInt(updateId)

            fetch(`http://localhost:5000/person/${customer_id}`, {
            method: 'PUT',
            body: JSON.stringify({
                id:parseInt(id),
                phone_number:parseInt(phone),
                email_address:email,
                customer_type:"person",
                first_name:fname,
                last_name:lname,
                date_of_birth:birth,
            }),
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
            })
            .then(function(response){ 
                return response.json()})
            .then(function(data){
                console.log(data)
                pBuildList()
            })
            .catch(error => console.error('Error:', error))
        }
    });


    const companyForm = document.getElementById('company_form')
 
    companyForm.addEventListener('submit', function(e){

        const id = document.querySelector('input[name="c_id"]').value
        const phone = document.querySelector('input[name="c_phone_number"]').value
        const email = document.querySelector('input[name="c_email_address"]').value
        const ico = document.querySelector('input[name="c_ICO"]').value
        const dic = document.querySelector('input[name="c_DIC"]').value
        const updateId = document.querySelector('input[name="c_put_id"]').value

        e.preventDefault()
        if (updateId == ""){
            fetch("http://localhost:5000/company", {
            method: 'POST',
            body: JSON.stringify({
                id:parseInt(id),
                phone_number:parseInt(phone),
                email_address:email,
                customer_type:"company",
                ICO:parseInt(ico),
                DIC:parseInt(dic),
            }),
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
            })
            .then(function(response){ 
                return response.json()})
            .then(function(data){
                console.log(data)
                cBuildList()
            })
            .catch(error => console.error('Error:', error))
        } else{
            const customer_id = parseInt(updateId)

            fetch(`http://localhost:5000/company/${customer_id}`, {
            method: 'PUT',
            body: JSON.stringify({
                id:parseInt(id),
                phone_number:parseInt(phone),
                email_address:email,
                customer_type:"company",
                ICO:parseInt(ico),
                DIC:parseInt(dic),
            }),
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
            })
            .then(function(response){ 
                return response.json()})
            .then(function(data){
                console.log(data)
                cBuildList()
            })
            .catch(error => console.error('Error:', error)) 
        }
    })


    const pGetAllButton = document.querySelector('button#p_get_all')
    
    const pBuildList = () => {
        var wrapper = document.getElementById('list-wrapper')
        wrapper.innerHTML = ''

        fetch('http://localhost:5000/person/', {
            method: 'GET',
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
            })
        .then((resp) => resp.json())
        .then(function(data){

        var list = data

        for (var i in list.data){
            var item = `<div class="task-wrapper flex-wrapper">
                            <h4 class="hide-show">ID ${list.data[i].id}: ${list.data[i].first_name} ${list.data[i].last_name}</h4>
                            <div style="display:none" class="get-box">
                                <table class="ui table">
                                    <tbody>
                                        <tr>
                                            <td>id: ${list.data[i].id}</td>
                                        </tr>
                                        <tr>
                                            <td>phone_number: ${list.data[i].phone_number}</td>
                                        </tr>
                                        <tr>
                                            <td>email_address: ${list.data[i].email_address}</td>
                                        </tr>
                                        <tr>
                                            <td>customer_type: ${list.data[i].customer_type}</td>
                                        </tr>

                                        <tr>
                                            <td>first_name: ${list.data[i].first_name}</td>
                                        </tr>
                                        <tr>
                                            <td>last_name: ${list.data[i].last_name}</td>
                                        </tr>
                                        <tr>
                                            <td>date_of_birth: ${list.data[i].date_of_birth}</td>
                                        </tr>
                                    </tbody>
                                </table>
                                </div>
                            <div style="flex:1">
                                <button style="width:20%;" class="ui primary button mb-5 detail">Detail</button>
                                <button style="width:20%;" class="ui primary button mb-5 delete">Delete</button>
                            </div>
                        </div> `
            
        wrapper.innerHTML += item

        let display = false
        $(".detail").click(function () {
            if (display===false) {
                $(this).parent().prev(".get-box").show("slow")
                display=true
            } else {
                $(".get-box").hide("slow");
                display=false
            }
        })
        }

        for (var i in list.data){
            var deleteBtn = document.getElementsByClassName('delete')[i]
            
            deleteBtn.addEventListener('click', (function(item){
              return function(){
                deleteItem(item)
              }
            })(list.data[i]))
        }
        })
        .catch(error => console.error('Error:', error));
    }


    const pGetIdInput = document.querySelector('input[name="p_get_id"]')
    const pGetIdButton = document.querySelector("button#p_get_id")
  
    const pGetCustomer = () => {
        const customer_id = pGetIdInput.value
        if (customer_id == "") {
            console.log('Empty field')
        }else {
        var wrapper = document.getElementById('list-wrapper')
        wrapper.innerHTML = ''

        fetch(`http://localhost:5000/person/${customer_id}`, {
            method: 'GET',
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
            })
        .then((resp) => resp.json())
        .then(function(data){
        
        var list = data
        console.log(list.id)
        if (list.id == 'undefined'){
            console.log(list.id)
        }   else{
        
            var item = `<div class="task-wrapper flex-wrapper">
                            <h4>ID ${list.id}: ${list.first_name} ${list.last_name}</h4>
                            <table class="ui table">
                                <tbody>
                                    <tr>
                                        <td>id: ${list.id}</td>
                                    </tr>
                                    <tr>
                                        <td>phone_number: ${list.phone_number}</td>
                                    </tr>
                                    <tr>
                                        <td>email_address: ${list.email_address}</td>
                                    </tr>
                                    <tr>
                                        <td>customer_type: ${list.customer_type}</td>
                                    </tr>
                                    <tr>
                                        <td>first_name: ${list.first_name}</td>
                                    </tr>
                                    <tr>
                                        <td>last_name: ${list.last_name}</td>
                                    </tr>
                                    <tr>
                                        <td>date_of_birth: ${list.date_of_birth}</td>
                                    </tr>
                                </tbody>
                            </table>
                            <div style="flex:1">
                                <button style="width:20%;" class="ui primary button mb-5 delete">Delete</button>
                            </div>
                        </div>`
    
        wrapper.innerHTML += item

        }

        var deleteBtn = document.getElementsByClassName('delete')[0]
        
        deleteBtn.addEventListener('click', (function(list){
            return function(){
            deleteItem(list)
            }
        })(list))
        })
        .catch(error => console.error('Error:', error))
    }
    }
    


    const cGetAllButton = document.querySelector('button#c_get_all')
    
    const cBuildList = () => {
        var wrapper = document.getElementById('list-wrapper')
        wrapper.innerHTML = ''

        fetch('http://localhost:5000/company/', {
            method: 'GET',
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
            })
        .then((resp) => resp.json())
        .then(function(data){

        var list = data

        for (var i in list.data){
            var item = `<div class="task-wrapper flex-wrapper">
                            <h4 class="hide-show">ID ${list.data[i].id} - ICO: ${list.data[i].ICO}</h4>
                            <div style="display:none" class="get-box">
                                <table class="ui table">
                                    <tbody>
                                        <tr>
                                            <td>id: ${list.data[i].id}</td>
                                        </tr>
                                        <tr>
                                            <td>phone_number: ${list.data[i].phone_number}</td>
                                        </tr>
                                        <tr>
                                            <td>email_address: ${list.data[i].email_address}</td>
                                        </tr>
                                        <tr>
                                            <td>customer_type: ${list.data[i].customer_type}</td>
                                        </tr>

                                        <tr>
                                            <td>ICO: ${list.data[i].ICO}</td>
                                        </tr>
                                        <tr>
                                            <td>DIC: ${list.data[i].DIC}</td>
                                        </tr>
                                    </tbody>
                                </table>
                                </div>
                            <div style="flex:1">
                                <button style="width:20%;" class="ui primary button mb-5 detail">Detail</button>
                                <button style="width:20%;" class="ui primary button mb-5 delete">Delete</button>
                            </div>
                        </div> `
            
        wrapper.innerHTML += item

        let display = false
        $(".detail").click(function () {
            if (display===false) {
                $(this).parent().prev(".get-box").show("slow")
                display=true
            } else {
                $(".get-box").hide("slow");
                display=false
            }
        })
        }

        for (var i in list.data){
            var deleteBtn = document.getElementsByClassName('delete')[i]
            
            deleteBtn.addEventListener('click', (function(item){
              return function(){
                deleteItem(item)
              }
            })(list.data[i]))
        }
        })
        .catch(error => console.error('Error:', error));
    }


    const cGetIdInput = document.querySelector('input[name="c_get_id"]')
    const cGetIdButton = document.querySelector("button#c_get_id")
  
    const cGetCustomer = () => {
        const customer_id = cGetIdInput.value
        if (customer_id == "") {
            console.log('Empty field')
        }else {
        var wrapper = document.getElementById('list-wrapper')
        wrapper.innerHTML = ''

        fetch(`http://localhost:5000/company/${customer_id}`, {
            method: 'GET',
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
            })
        .then((resp) => resp.json())
        .then(function(data){
        
        var list = data
            var item = `<div class="task-wrapper flex-wrapper">
                            <h4>ID ${list.id} - ICO: ${list.ICO}</h4>
                            <table class="ui table">
                                <tbody>
                                    <tr>
                                        <td>id: ${list.id}</td>
                                    </tr>
                                    <tr>
                                        <td>phone_number: ${list.phone_number}</td>
                                    </tr>
                                    <tr>
                                        <td>email_address: ${list.email_address}</td>
                                    </tr>
                                    <tr>
                                        <td>customer_type: ${list.customer_type}</td>
                                    </tr>
                                    <tr>
                                        <td>ICO: ${list.ICO}</td>
                                    </tr>
                                    <tr>
                                        <td>DIC: ${list.DIC}</td>
                                    </tr>
                                </tbody>
                            </table>
                            <div style="flex:1">
                                <button style="width:20%;" class="ui primary button mb-5 delete">Delete</button>
                            </div>
                        </div>`
    
        wrapper.innerHTML += item

        var deleteBtn = document.getElementsByClassName('delete')[0]
        
        deleteBtn.addEventListener('click', (function(list){
            return function(){
            deleteItem(list)
            }
        })(list))
        })
        .catch(error => console.error('Error:', error))
    }
    }


    const deleteIdInput = document.querySelector('input[name="delete_id"]')
    const deleteIdButton = document.querySelector("button#delete_id")
  
    const deleteCustomer = () => {
        const customer_id = deleteIdInput.value
        if (customer_id == "") {
            console.log('Empty field')
        }else {
        fetch(`http://localhost:5000/person/${customer_id}`, {
            method: 'DELETE',
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
        })
        .then(function(){
            var item = `<div class="task-wrapper flex-wrapper">
                            <h4>Customer with ID ${customer_id} was deleted.</h4>
                        </div>`
            var wrapper = document.getElementById('list-wrapper')
            wrapper.innerHTML = ''
            wrapper.innerHTML += item
        })
        .catch(error => console.error('Error:', error))
        console.log(`Successfully deleted customer with ID: ${customer_id}`)
    }
    }


    function deleteItem(item){
        fetch(`http://localhost:5000/person/${item.id}`, {
            method: 'DELETE',
            headers:{
                'Content-type': 'application/json; charset=UTF-8',
            }
        }).then((response) => {
        pBuildList()
        })
        .catch(error => console.error('Error:', error))
    }

    cGetAllButton.addEventListener("click", cBuildList)
    cGetIdButton.addEventListener("click", cGetCustomer)
    pGetAllButton.addEventListener("click", pBuildList)
    pGetIdButton.addEventListener("click", pGetCustomer)
    deleteIdButton.addEventListener("click", deleteCustomer)
});