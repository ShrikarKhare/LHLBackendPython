let creditLimit = 5000;

const loanOut = (amount) => {
    return new Promise ((resolve,reject) => {
        if (creditLimit <= 0) {
            reject("you have Insufficient funds");
        } else if (creditLimit <= amount) {
        //amount is greater than the limit, but does not take the account into negative
            let maxWithdrawal = creditLimit 
            creditLimit -= maxWithdrawal 
            resolve(maxWithdrawal);
        } else {
            creditLimit -= amount;
            resolve(amount);
        }
    });
};

console.log("Asking for $150, which should be okay ...");
loanOut(150)
  .then((amountReceived) => {
    console.log(`\t-> I got $${amountReceived} loan from the bank! Remaining Credit Limit: $${creditLimit}`);
  })
  .catch((err) => {
    console.log(`\t-> Error: ${err}!`);
  });