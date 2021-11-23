const chai = require('chai');
const assert = chai.assert;
const gameResults = require('../rockPaperScissors');
let rock = 'rock';
let paper = 'paper';
let scissors = 'scissors';
let player1Wins = 'Player 1 wins the game!';
let player2Wins = 'Player 2 wins the game!';
let tie = 'It is a tie!'; 
describe('#RockPaperScissors', () => {
    it('should return Player 1 wins for "rock" "scissors"' ,() =>{
        assert(gameResults(rock,scissors), player1Wins);
    })
    it('should return Player 2 wins for "paper" "scissors"' ,() =>{
        assert(gameResults(paper,scissors), player2Wins);
    })
    it('should return a tie for "scissors" "scissors"' ,() =>{
        assert(gameResults(scissors,scissors), tie);
    })
    it('should return Player 1 wins for "scissors" "paper"' ,() =>{
        assert(gameResults(scissors,paper), player1Wins);
    })
    it('should return Player 2 wins for "scissors" "rock"' ,() =>{
        assert(gameResults(scissors,rock), player2Wins);
    })
    it('should return a tie for "rock" "rock"' ,() =>{
        assert(gameResults(rock,rock), tie);
    })
    it('should return Player 1 wins for "paper" "rock"' ,() =>{
        assert(gameResults(paper,rock), player1Wins);
    })
    it('should return Player 2 wins for "paper" "scissor"' ,() =>{
        assert(gameResults(paper,scissors), player2Wins);
    })
    it('should return a tie for "paper" "paper"' ,() =>{
        assert(gameResults(paper,paper), tie);
    })
    it('should return undefined for missing parameter', () => {
        assert(gameResults(paper), undefined);
    })
})