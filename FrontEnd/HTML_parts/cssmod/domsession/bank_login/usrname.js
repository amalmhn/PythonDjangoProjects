class Bank {

    static getData() {
        var users = {
            userone: { username: 'userone', password: 'test', mpin: '201348', acno: '1000', balance: '1000' },
            usertwo: { username: 'usertwo', password: 'test1', mpin: '20145', acno: '1001', balance: '20000' },
            userthree: { username: 'userthree', password: 'test2', mpin: '2020', acno: '1002', balance: '3000' }

        }
        return users
    }

    static authenticareUser(username,password){
        alert('authentication')
        var data=Bank.getData()
        if(username in data){
            let pwd=data[username]['password']
            if(pwd==password){

                return 0
            }
            else{
                return -1
            }
        }else{
            return 1
        }
    }

    static login(){
        alert('inside login')
        let uname=document.querySelector('#uname').value
        let pwd=document.querySelector('#pwd').value
        var user=Bank.authenticareUser(uname,pwd)
        if (user==1){
            alert('user does not exist')
        }
        else if(user==-1){
            alert('Invalid Password')
        }
        else if(user==0){
            alert('logi Success')
            window.location.href='scnd_page.html'
        }

    }

    static deposit(){
        // alert('deposit')
        let uname=document.querySelector('#usrname').value
        let pwd=document.querySelector('#pword').value
        let check=Bank.authenticareUser(uname,pwd)
        if(check==0){
            alert('Deposit successfull')
        }else if(check==-1){
            alert('Invalid Password')
        }else{
            alert('Somethig went wrong')
        }

    }

    static withdraw(){
        // alert('wi')
        let uname=document.querySelector('#usrname').value
        let pwd=document.querySelector('#pword').value
        let check=Bank.authenticareUser(uname,pwd)
        if(check==0){
            alert('Withdraw successfull')
        }else if(check==-1){
            alert('Invalid Password')
        }else{
            alert('Somethig went wrong')
        }

    }
}
