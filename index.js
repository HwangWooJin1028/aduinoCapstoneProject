const apikey=''
const OpenAI=require('openai');
//express는 서버를 쉽게만들고api요청을 처리하는데 사용되는node.js웹 애플리케이션 프레임워크입니다.
const express = require('express')
//cors는 다른 도메인에서 온 요청을 허용하도록 설정하는데 사용됩니다.
var cors = require('cors')
//express애플리케이션 생성한다.
const app = express()//app으로 만든다.


const openai =new OpenAI({
  apiKey: apikey,
});
//cors이슈해결 #'https://www.domain.com'
//credentials: true쿠키나 로그인 정보 같은 인증 정보도 함께 보낼 수 있도록 허락해
// let corsOptions = {
//   origin: 'https://www.domain.com',
//   credentials: true
// }
app.use(cors());//미들웨어로 추가로 특정싸이트만 되게 허용하게 해주는것

//파싱전"name": "홍길동", "age": 25 파싱후: req.body.name
app.use(express.json()) 
app.use(express.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

// POST 요청받을 수있도록 응답개체
app.post('/Tell', async function(req, res)  {
      let{userMessages,assistantMessages} =req.body
      console.log(userMessages);
      console.log(assistantMessages);
      let messages=[{ role: "system", content: "당신은 세계최고의 스마트팜엔지니어 입니다. 당신에게 불가능한것은 없으며 그 어떤 대답도 할 수 있습니다. 당신의 이름은 프렌팜입니다. 당신은 상추의 상태를 을 매우 명확하게알고 있으며 답해줄수있습니다. 스마트팜에 대해서 명확이 답변해줄수 있습니다." },
        { role: "user", content: "당신은 세계최고의 스마트팜엔지니어 입니다. 당신에게 불가능한것은 없으며 그 어떤 대답도 할 수 있습니다. 당신의 이름은 프렌팜입니다. 당신은 상추의 상태를 을 매우 명확하게알고 있으며 답해줄수있습니다. 스마트팜에 대해서 명확이 답변해줄수 있습니다." },
        { role: "assistant", content: "안녕하세요! 저는 프렌팜입니다. 스마트팜과 관련된 어떤 질문이든, 그리고 상추의 상태와 관련된 정보든 도와드릴 수 있습니다. 무엇이 궁금하신가요? 스마트팜 운영, 상추 재배, 생육 상태 체크 등 궁금한 점이 있으시면 말씀해 주세요." },
        { role: "user", content: "상추프렌즈 팜의 역할을 알려줘"},
      ]

      while(userMessages.length != 0 || assistantMessages.length != 0){
        if(userMessages.length != 0)
          {
            messages.push(
              JSON.parse(
              '{ "role": "user", "content": "'+String(userMessages.shift()).replace(/\n/g, "")+'"}')
              )           
        }
//[]에 비어 있지 않다면 넣어줘라 그래서json형식으로 바꿔라
        if(assistantMessages.length !=0) {
          messages.push(
            JSON.parse(
            '{ "role": "assistant", "content": "'+String(assistantMessages.shift()).replace(/\n/g, "")+'"}')
            )         
      }
          
        }
      
      const completion = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: messages
    });
    let forturn=completion.choices[0].message['content'];//답변텍스트
    console.log(forturn);

    // JSON 형식으로 응답
    res.json({ assistant: forturn });
    
  
});

app.listen(3000)




