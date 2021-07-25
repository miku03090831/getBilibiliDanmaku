<template>
  <div class="detail">
    <el-container>
      <el-header class="title">名字</el-header>
      <el-container class="bottom">
        <el-aside class="number">Aside</el-aside>
        <el-main class="hot-word" id="hot-word">Main</el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import * as echarts from "echarts";
import "echarts-wordcloud/dist/echarts-wordcloud";
import "echarts-wordcloud/dist/echarts-wordcloud.min";
export default {
  methods: {
    wordGraphInit() {
      let hotword = echarts.init(document.getElementById("hot-word"));
      hotword.clear();

      var keywords = [
        { name: "男神", value: 2.64 },
        { name: "好身材", value: 4.03 },
        { name: "校草", value: 24.95 },
        { name: "酷", value: 4.04 },
        { name: "时尚", value: 5.27 },
        { name: "阳光活力", value: 5.8 },
        { name: "初恋", value: 3.09 },
        { name: "英俊潇洒", value: 24.71 },
        { name: "霸气", value: 6.33 },
        { name: "腼腆", value: 2.55 },
        { name: "蠢萌", value: 3.88 },
        { name: "青春", value: 8.04 },
        { name: "网红", value: 5.87 },
        { name: "萌", value: 6.97 },
        { name: "认真", value: 2.53 },
        { name: "古典", value: 2.49 },
        { name: "温柔", value: 3.91 },
        { name: "有个性", value: 3.25 },
        { name: "可爱", value: 9.93 },
        { name: "幽默诙谐", value: 3.65 },
      ];
      var option = {
        series: [
          {
            type: "wordCloud",
            sizeRange: [15, 80],
            rotationRange: [0, 0],
            rotationStep: 45,
            gridSize: 8,
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
            data: keywords,
          },
        ],
      };

      hotword.setOption(option);
    },
  },
  mounted() {
    this.wordGraphInit();
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