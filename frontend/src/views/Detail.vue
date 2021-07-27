<template>
  <div class="detail">
      <div class="title">
        <div class="wrap-title">{{ this.name }}</div>
      </div>
      <div class="container bottom">
        <div class="side number">
          <div class="fans">
            <div class="fans-word">
              the number of this vtuber's hardcore fans is
              <b>{{ this.fans_num }}</b
              >, and <b>{{ this.single_rate }}%</b> of them are DanTuiRen
            </div>
            <div id="fans-graph"></div>
          </div>
          <div class="danmaku">
            <div>
              <b>{{ this.posi_rate }}%</b> of the danmakus expressed their love
              directly
            </div>
            <div>others didn't express their love directly in words</div>
            <div>maybe they are a little shy, they prefer a gentler way</div>
            <div id="posi-graph"></div>
          </div>
        </div>
        <div class="main hot-word" id="hot-word"></div>
      </div>
    </div>
</template>

<script>
import * as echarts from "echarts";
import "echarts-wordcloud/dist/echarts-wordcloud";
import "echarts-wordcloud/dist/echarts-wordcloud.min";
export default {
  data() {
    return {
      name: "",
      posi_rate: 0,
      fans_num: 0,
      rate: 0,
      uid: this.$route.query.uid,
      keywords: [],
    };
  },
  computed: {
    single_rate() {
      return Math.ceil(10000 * this.rate) / 100;
    },
    single_num() {
      return Math.ceil(this.fans_num * this.rate);
    },
    non_single_num() {
      return this.fans_num - this.single_num;
    },
    gentle() {
      return 100 - this.posi_rate;
    },
  },
  methods: {
    wordGraphInit() {
      let hotword = echarts.init(document.getElementById("hot-word"));
      hotword.clear();

      var option = {
        backgroundColor: "rgba(211,225,230)",
        backgroundColor: {
          colorStops: [
            {
              offset: 0,
              color: "rgba(211,225,230)", // 0% 处的颜色
            },
            {
              offset: 1,
              color: 'rgb(254,214,227)', // 100% 处的颜色
            },
          ],
          global: false, // 缺省为 false
        },
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
    getHotWord() {
      this.$axios
        .post("api/hotword", {
          uid: this.uid,
        })
        .then((res) => {
          for (let key in res.data) {
            this.keywords.push({ name: key, value: res.data[key] });
          }
          this.wordGraphInit();
        });
    },
    getInfo() {
      this.$axios
        .post("api/getinfo", {
          uid: this.uid,
        })
        .then((res) => {
          console.log(res.data);
          this.fans_num = res.data["fans_num"];
          this.rate = res.data["rate"];
          this.name = res.data["name"];
          this.fans_init();
        });
    },
    getSentiment() {
      this.$axios
        .post("api/getSentiment", {
          uid: this.uid,
        })
        .then((res) => {
          this.posi_rate = Math.ceil(100 * res.data) / 100;
          this.posi_init();
        });
    },
    fans_init() {
      let fans = echarts.init(document.getElementById("fans-graph"));
      var option = {
        series: [
          {
            name: "单推人比例",
            type: "pie",
            radius: "50%",
            data: [
              { value: this.single_num, name: "DanTuiRen" },
              { value: this.non_single_num, name: "others" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };
      fans.setOption(option);
    },
    posi_init() {
      let posi = echarts.init(document.getElementById("posi-graph"));
      posi.clear();

      var option = {
        series: [
          {
            name: "积极比例",
            type: "pie",
            radius: "50%",
            data: [
              { value: this.posi_rate, name: "direct love" },
              { value: this.gentle, name: "gentler way" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };
      posi.setOption(option);
    },
  },
  mounted() {
    this.getHotWord(); //跟挂载到dom有关，需要在mount之后
    this.getInfo();
    this.getSentiment();
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=ZCOOL+KuaiLe&display=swap');
* {
  margin: 0;
  padding: 0;
}
.detail {
  position: absolute;
  height: 100%;
  width: 100%;
}
#fans-graph {
  position: absolute;
  top: 15%;
  left: 24%;
  width: 400px;
  height: 300px;
}
#posi-graph {
  position: absolute;
  top: 15%;
  left: 30%;
  width: 300px;
  height: 300px;
  overflow: hidden;
}

.fans-word {
  position: absolute;
  top: 10%;
  left: 10%;
  height: 10%;
  width: 80%;
}

.title {
  position: absolute;
  text-align: center;
  line-height: 100px;
  height: 15% !important;
  width: 100%;
  /* background-image: linear-gradient(to right, #ebbba7 0%, #cfc7f8 100%); */
  background-image: linear-gradient(to right, #a8edea 0%, #fed6e3 100%);
}
.wrap-title {
  font-size: 60px;
  background-image: linear-gradient(135deg, red, blue);
  -webkit-background-clip: text;
  color: transparent;
  font-family: 'ZCOOL KuaiLe', cursive;
}

.bottom {
  position: absolute;
  top: 15%;
  height: 85%;
  width: 100%;
  background-image: linear-gradient(to right, #a8edea 0%, #fed6e3 100%);
}
.side {
  overflow: hidden;
  position: absolute;
  top: 0%;
  left: 0%;
  width: 50% !important;
  height: 100%;
  line-height: 30px;
  color: #333;
  text-align: center;
}

.fans {
  position: absolute;
  height: 35%;
  width: 100%;
  top: 0%;
  left: 0%;
}

.danmaku {
  position: absolute;
  height: 50%;
  width: 100%;
  top: 50%;
  left: 0%;
}

.main {
  position: absolute;
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  width: 50% !important;
  height: 100%;
  left: 50%;
  top: 0%;
  overflow: hidden;
}
</style>