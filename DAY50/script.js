const Deposit = document.getElementById('Deposit')
const Withdraw = document.getElementById('Withdraw')
const input = document.getElementById('input')
let boutput = document.getElementById('Balance-output')

let Balance = 0

Deposit.addEventListener('click', function(){
    Balance = Balance + Number(input.value)
    boutput.textContent = Balance
})
Withdraw.addEventListener('click', function(){
    Balance = Balance - Number(input.value)
    boutput.textContent = Balance
})