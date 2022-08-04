export function checkLoggedIn(){
    if(localStorage.getItem('token')==null){
        this.loggedIn = false
    }else{
        this.loggedIn = true
    }
}