function solution(a, b) {
    let str_a = a.toString()
    let str_b = b.toString()
    let b_first = str_b+str_a
    let a_first = str_a+str_b
    if(b_first > a_first) {
        return Number(b_first)
    } return Number(a_first)
}