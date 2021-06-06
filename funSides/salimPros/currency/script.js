/* get the input from the user
only allow the num keys to be used
prompt: input coins as decimal with main currency or seperate coins as their name i.e 12.34 for 12 dollars 34 cents or
enter it as 12dollars 34 cents.
or let's startwith input as 12 dollars and denom separated
*/

var document, n2uIn,n2uBtn,u2nIn,u2nBtn;

n2uIn = document.querySelectorAll("#NGN"); // problem is that this isnt outputing the class but its elements as an array, how to get only class for editing?
n2uBtn = document.querySelector(".ngnToDollar");
u2nIn = document.querySelectorAll("#USD");
u2nBtn = document.querySelector(".usdToNaira");

toggleDisplay = function (inputBox) {
    for(i=0;i<1;i++){
        inputBox(i).classList.toggle("notInput")
        inputBox(i).classList.toggle("get-userInput")
    }
}


n2uBtn.addEventListener("click",e => {
    toggleDisplay(n2uIn);
})