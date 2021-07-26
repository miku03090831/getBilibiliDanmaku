<template>
  <div class="detail">
    <el-container>
      <el-header class="title">{{this.name}}</el-header>
      <el-container class="bottom">
        <el-aside class="number">
          the number of this vtuber's hardcore fans is {{this.fans_num}},
          and{{this.single_rate}}% of them are single-minded
        </el-aside>
        <el-main class="hot-word" id="hot-word"></el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import * as echarts from "echarts";
import "echarts-wordcloud/dist/echarts-wordcloud";
import "echarts-wordcloud/dist/echarts-wordcloud.min";
export default {
  data(){
    return{
      name:"",
      fans_num:0,
      rate:0,
      uid: this.$route.query.uid,
      keywords:[
      ]
    }
  },
  computed:{
    single_rate(){
      return Math.ceil(10000*this.rate)/100;
    }
  },
  methods: {
    wordGraphInit() {
      let hotword = echarts.init(document.getElementById("hot-word"));
      hotword.clear();

      
      var option = {
        series: [
          {
            type: "wordCloud",
            sizeRange: [15, 100],
            rotationRange: [0, 0],
            rotationStep: 45,
            gridSize: 20,
            shape: "pentagon",
            width: "100%",
            height: "100%",
            textStyle: {
              normal: {
                color: function () {
                  return (
                    "rgb(" +
                    [
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160),
                      Math.round(Math.random() * 160),
                    ].join(",") +
                    ")"
                  );
                },
              },
            },
            data: this.keywords,
          },
        ],
      };
      hotword.setOption(option);
    },
    getHotWord(){
      this.$axios.post("api/hotword",{
          'uid': this.uid
        }).then(res=>{
          for(let key in res.data){
            this.keywords.push({"name":key,"value":res.data[key]})
          }
          this.wordGraphInit(); 
        })
    },
    getInfo(){
      this.$axios.post("api/getinfo",{
          'uid': this.uid
        }).then(res=>{
          console.log(res.data)
          this.fans_num = res.data["fans_num"]
          this.rate = res.data["rate"]
          this.name = res.data["name"]
        })
    }
  },
  mounted() {
    this.getHotWord();//跟挂载到dom有关，需要在mount之后
    this.getInfo()
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.detail {
  position: absolute;
  height: 100%;
  width: 100%;
}
.el-header {
  position: absolute;
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 100px;
  height: 15% !important;
  width: 100%;
}

.bottom {
  position: absolute;
  top: 15%;
  height: 85%;
  width: 100%;
}
.el-aside {
  position: absolute;
  top: 0%;
  left: 0%;
  width: 40% !important;
  height: 100%;

  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  position: absolute;
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  width: 60% !important;
  height: 100%;
  left: 40%;
  top: 0%;
}
</style>