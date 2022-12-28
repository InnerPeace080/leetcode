const test = require('./2512.json') 


let getPointTime = 0
let splitTime = 0
let mapTime = 0
let insertTime = 0

function getPoint(positive_feedback_map,negative_feedback_map, reportString){
  const startTime = Date.now()
  let keyArr = reportString.split(' ')
  splitTime+=Date.now()-startTime

  let wordMap = {}
  keyArr.forEach((w)=>{
      wordMap[w] = (wordMap[w]||0) + 1
  })
  mapTime+=Date.now()-startTime
  // const ret = positive_feedback.reduce((t,f)=> (t+ (wordMap[f]||0) * 3 ),0) + negative_feedback.reduce((t,f)=> t+ (wordMap[f]||0) * (-1) ,0)    

  const ret = keyArr.reduce((t,w)=> t+ (positive_feedback_map[w]||0) * 3 + (negative_feedback_map[w]||0) * (-1) ,0)

  getPointTime+=Date.now()-startTime
  return ret
}

var studentPointMap={}


function isGreater(userId1,userId2){
  if(studentPointMap[userId1] === studentPointMap[userId2]){
      return userId1<userId2
  }
  return studentPointMap[userId1] > studentPointMap[userId2]
}

function MinHeap(k) {
  this.heap = []
  this.insert = function (num){        
      const startTime = Date.now()
      if(this.heap.length===k){
          this.removeMinAndPushToTop(num)
      }else if(this.heap.length>=1){
          this.heap.push(num)
          // console.log('this.heap insert before',this.heap,this.heap.map(c=>studentPointMap[c]))
          let idx = this.heap.length - 1
          while(idx>0){
              const currentVal = this.heap[idx]
              const parentVal = this.heap[Math.floor((idx-1)/2)]
              if(isGreater(parentVal,currentVal)){
                  [this.heap[Math.floor((idx-1)/2)], this.heap[idx] ] = [this.heap[idx], this.heap[Math.floor((idx-1)/2)]]    
              }else{
                  break;
              }
              
              idx = Math.floor((idx-1)/2)
          }
      }else{
          this.heap.push(num)
      }
      // console.log('this.heap insert',this.heap,this.heap.map(c=>studentPointMap[c]))
      insertTime+=Date.now()-startTime
      
  }
  this.removeMinAndPushToTop = function (num){
      this.heap[0]=num
      // this.heap.pop()
      let idx = 0
      while(idx<(this.heap.length-1)){
          const currentVal = this.heap[idx]
          const leftVal = this.heap[idx*2+1]
          const rightVal = this.heap[idx*2+2]
          if((leftVal !== undefined) && (isGreater(currentVal , leftVal)  || isGreater(currentVal , rightVal) )){
              if(isGreater(currentVal, leftVal) && (rightVal === undefined || isGreater(rightVal,leftVal  ))){
                  [this.heap[idx*2+1],this.heap[idx]] = [this.heap[idx],this.heap[idx*2+1]]
                  idx = idx*2+1
              }else{
                  [this.heap[idx*2+2],this.heap[idx]] = [this.heap[idx],this.heap[idx*2+2]]
                  idx = idx*2+2
              }
          }else{
              break;
          }
      }
  }
}

/**
 * @param {string[]} positive_feedback
 * @param {string[]} negative_feedback
 * @param {string[]} report
 * @param {number[]} student_id
 * @param {number} k
 * @return {number[]}
 */
var topStudents = function(positive_feedback, negative_feedback, report, student_id, k) {    
  studentPointMap={}
  console.time('topStudents')
  const kMinHeap = new MinHeap(k)

  // convert positive_feedback and negative_feedback to map
  const positive_feedback_map = {}
  const negative_feedback_map = {}
  positive_feedback.forEach((w)=>{
      positive_feedback_map[w] = 1
  })
  negative_feedback.forEach((w)=>{
      negative_feedback_map[w] = 1
  })


  for(let i =0; i< student_id.length;i++){
      studentPointMap[student_id[i]] = getPoint(positive_feedback_map,negative_feedback_map,report[i])
      if(isGreater(student_id[i],kMinHeap.heap[0]) || kMinHeap.heap.length < k){
          kMinHeap.insert(student_id[i])  
          // console.log('kMinHeap.heap',kMinHeap.heap,kMinHeap.heap.map(c=>studentPointMap[c]))
      }
  }
  console.timeEnd('topStudents')
  // console.log('studentPointMap',studentPointMap)
  
  
  return kMinHeap.heap.sort((userId1,userId2)=>(isGreater(userId1,userId2)?-1:1))
  
};

console.time('start')
const ret= topStudents(test.positive_feedback,test.negative_feedback,test.report,test.student_id,test.k)
console.timeEnd('start')

console.log('ret',ret)

console.log('splitTime',splitTime)
console.log('mapTime',mapTime)
console.log('getPointTime',getPointTime)

console.log('insertTime',insertTime)