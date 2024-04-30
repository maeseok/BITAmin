function max(first, ...rests) {
    // 변수 선언하기
    let output
    let items

    if (Array.isArray(first)) {
      output = first[0]
      items = first
    } else if (typeof(first) === 'string') {
      output = first
      items = rests
    }

    for (const item of items) {
      if (output < item) {
        output = item
      }
    }
    return output
  }
  const strings = ['딸기','바닐라','초코','피스타치오']
  console.log(`max(문자열): ${max(strings)}`)
  console.log(`max(문자열, ...): ${max(...strings)}`)