<template>
  <div class="single-question mt-2">
    <div v-if="question" class="container">
      <h1>{{ question.content }}</h1>
      <question-actions
      v-if="isQuestionAuthor"
      :slug="question.slug"/>
      <p class="mb-0">
        Posted by:
        <span class="author-name">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
       <hr>
       <div v-if="userHasAnswered"><p class="answer-added">You have written an answer</p></div>
       <div v-else-if="showForm">
         <form class="card" @submit.prevent="onSubmit">
           <div class="card-header px-3">
             Answer the Question
           </div>
           <div class="card-block">
             <textarea 
             class="form-control"
             v-model="newAnswerBody"
             placeholder="Answer the Question">
             </textarea>
           </div>
           <div class="card-footer px-3">
             <button class="btn btn-sm btn-success" type="submit">Submit Your Answer</button>
           </div>
         </form>
         <p v-if="error" class="error mt-2">{{error}}</p>
       </div>
       <div v-else>
         <button class="btn btn-sm btn-success" @click="showForm=true">
           Answer the Question</button>
       </div>
       <hr>
    </div>
    <div class="container">
      <AnswerComponent 
        v-for="answer in answers"
        :answer="answer" 
        :requestUser = "requestUser"
        :key="answer.id"
        @delete-answer="deleteAnswer" />
       <div class="my-4">
        <p v-show="loadingAnswers">...loading...</p>
        <button
        v-show="next"
        @click="getQuestionAnswers" 
        class="btn btn-sm btn-outline-success"
        >Load more</button>
      </div>
    </div>
  </div>
</template>
<script>
import { apiService } from "@/common/api.service.js";
import AnswerComponent from "@/components/Answer.vue"
import QuestionActions from "@/components/QuestionActions.vue"
export default {
  name: "Question",
  props: {
    slug: {
      type: String,
      required: true,
    },
  },
  components:{
    AnswerComponent,
    QuestionActions
  },
  data() {
    return {
      question: {},
      answers: [],
      newAnswerBody:null, //to store the answer. basically we'll have a form whwre a user can submit the answer but that  
      error:null,         // form will be shown only if the user has not already answered that question 
      userHasAnswered: false, 
      showForm: false , // form will be show when user presses the answer button and showForm will be set to true
      next:null,
      loadingAnswers:false,
      requestUser: null
   };
  },
   computed: {
        isQuestionAuthor(){
            return this.question.author === this.requestUser;
        }
    },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    setRequestUser(){
      this.requestUser = window.localStorage.getItem("username")
    },
    getQuestionData() {
      let endpoint = `/api/questions/${this.slug}/`;
      this.loadingAnswers = true
      apiService(endpoint).then((data) => {
        if(data) {
          this.question = data;
          this.userHasAnswered = data.user_has_answered
          this.setPageTitle(data.content);
        }
       else {
         this.question = null
         this.setPageTitle('404 - Not Found')
         this.$router.push('/:catchAll(.*)')
       }
      });
    },
    getQuestionAnswers(){
      let endpoint = `/api/questions/${this.slug}/answers/`;
       if(this.next){
          endpoint = this.next
        }
      apiService(endpoint)
      .then(data=>{
        this.answers.push(...data.results)
        this.loadingAnswers = false
        if(data.next){
          this.next = data.next;
        } else {
          this.next = null
        }
      })
      
    },
    onSubmit(){
      if(this.newAnswerBody){
        let endpoint = `/api/questions/${this.slug}/answer/`
        apiService(endpoint, "POST", {body: this.newAnswerBody})
        .then(data=>{
          this.answers.unshift(data)
        })
        this.newAnswerBody = null
        this.showForm = false
        this.userHasAnswered = true
        if(this.error)this.error = null
      } else {
        this.error = "This field cannot be empty!"
      }
    },
    async deleteAnswer(answer) {
      let endpoint  = `/api/answers/${answer.id}/`;
      try {
          await apiService(endpoint, "DELETE");
          this.answers.splice(this.answers.indexOf(answer), 1)
          // this.$delete(this.answers, this.answers.indexOf(answer)); //$delete allows us to delete an element from an array(the array is answers)
          this.userHasAnswered = false;
      }
      catch(error) {
        console.log(error);
        
      }
    }
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
    this.setRequestUser();
  },
};
</script>

<style scoped>
.author-name {
  font-weight: bold;
  color: #dc3545;
}
.answer-added{
  font-weight: bold;
  color: green;
}
.error {
  font-weight: bold;
  color: red;
}
</style>