<template>
  <div class="home mt-2">
    <div class="container">
      <div v-for="question in questions" :key="question.pk" class="container">
        <p class="mb-0">
          Posted by:
          <span class="question-author">{{ question.author }}</span>
        </p>
        <h2>
          <router-link
            :to="{ name: 'question', params: { slug: question.slug } }"
            class="question-link"
            >{{ question.content }}</router-link
          >
        </h2>
        <p>Answers: {{ question.answers_count }}</p>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">...loading...</p>
        <button
        v-show="next"
        @click="getQuestions" 
        class="btn btn-sm btn-outline-success"
        >Load more</button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "home",
  data() {
    return {
      questions: [],
      next:null,
      loadingQuestions:false
    };
  },
  methods: {
    // get Questions method can be called again by clicking load more button and it gets called only if next is not null 
    getQuestions() {
      // make a GET Request to the questions list endpoint and populate the questions array
      let endpoint = "/api/questions/";
      if(this.next)endpoint = this.next
      this.loadingQuestions=true;
      apiService(endpoint).then((data) => {
        this.questions.push(...data.results);
        this.loadingQuestions = false
        if(data.next){
          this.next = data.next;
        } else {
          this.next = null
        }
      });
    },
  },
  created() {
    this.getQuestions();
    document.title = "Quesko";
  },
};
</script>

<style scoped>
.question-name {
  font-weight: bold;
  color: #dc3545;
}
.question-author {
  font-weight: bold;
  color: #dc3545;
}

.question-link {
  font-weight: bold;
  color: black;
}

.question-link:hover {
  color: #343a40;
  text-decoration: none;
}
.question-link {
  font-weight: bold;
  color: black;
}
question-link:hover {
  color: #dc3545;
  /* text-decoration: none; */
}
/* .ques {

} */
</style>
