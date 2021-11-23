const gameResults = (player1,player2) =>{

    if (player1 === player2){
       return 'It is a tie!';
    }
 
    if (player1 === 'rock' && player2 === 'paper'){
       return 'Player 2 wins the game!';
    }
 
    if (player1 === 'paper' && player2 === 'scissors')
    {
       return 'Player 2 wins the game!';
    }
 
    if (player1 === 'scissors' && player2 === 'rock')
    {
       return 'Player 2 wins the game!';
    }
 
    return 'Player 1 wins the game!';
 }

 module.exports = gameResults;