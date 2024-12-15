function getRandomNumbers(){
    const numbers=[];
    for(let i=0;i<10;i++){
        const num = Math.random()
        numbers[i]=Math.floor(num*100+1)
    }
    return numbers
}
function getEvenNumbers(numbers){
    const Evennumbers=numbers.filter(function(value){
        return value%2===0;
    })
    return Evennumbers;
}

function getAverage(numbers){
    const sum=numbers.reduce(function(total,num){
        return total+num;
    },0);
    const aver = sum/numbers.length;
    return aver.toFixed(1);
}

const numbers=getRandomNumbers()
console.log(`10개의 난수들: ${numbers}`);
const Evennumbers=getEvenNumbers(numbers);
console.log(`짝수 난수들: ${Evennumbers}`);
const aver = getAverage(Evennumbers);
console.log(`짝수 난수들의 평균:${aver}`);
