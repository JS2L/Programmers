function solution(num_list) {
    let even = 0;
    let odd = 0

    num_list.map((v, i) => {
        (i % 2) ? even += v : odd += v; 
    })

    return Math.max(even,odd)
}