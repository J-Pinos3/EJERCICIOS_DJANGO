

var updateBtns = document.getElementsByClassName('update-cart')
for(let i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        //where productId an action are the atributes I created in store.html
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'Action:', action)

        console.log("USER", user)
        if( user === 'AnonymousUser' ){
            console.log("Not Logged in")
        }else{
            updateUserOrder(productId, action)
        }

    })
}

//this function will do a POST request to api /update_item/
//then we'll get the item as json format
//without the csrf token we wont be able to make this request
//I'll create the token inside main.html
function updateUserOrder(productId, action){
    console.log('User is authsenticated, sending data...')

    var url = '/update_item/'

    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'productId':productId, 'action': action})
        //body is the data we send to backend
    })
    .then((response)=>{
        return response.json
    })
    .then((data)=>{
        console.log('Data:', data)
        location.reload()
    })
}