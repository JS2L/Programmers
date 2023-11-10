function solution(myString) {
    a=[]
    let str = myString.split('')
    for(let i =0; i < str.length; i++) {
        if(str[i] < "l") {
            a.push("l")
        } else {
            a.push(str[i])
        }
    } return a.join('')
}