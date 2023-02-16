<template>
  <div style="display: flex; justify-content: center;">
    <el-row style="max-width: 1100px; min-width: 1000px">
    <el-col  :span="14">
      <el-row class="shadedbox" style="height: 250px; display: flex; flex-direction: column;">
        <div class="controlBoxHead">
        <h3 style="float: left; margin-left: 20px">Recent Visitors</h3>
        <img src="../assets/icon/refresh.png" class="optionBtn" @click="getVisitorData">
        </div>
        <div style="display: flex; flex-direction: row;">
            <div class="visitorInfo" v-for="visitor in visitorList.slice(0,4)" :key="visitor.id">
              <div v-if="visitor.image">
                <img :src='visitor.image' class="photo">
                <!-- <img :src='testImg' class="photo"> -->
              </div>
              <div v-if="!visitor.image">
                <img src='../assets/icon/user.png' class="photo">
                <!-- <img :src='testImg' class="photo"> -->
              </div>
              {{visitor.name }}
            </div>
            <div class="visitorInfo">
              <img src="../assets/icon/more.png" class="photo" >
              <p style="font-size: 12px; margin-top: 1px;">More Visitors</p>
            </div>
        </div>
      </el-row>
      <el-row class="shadedbox" style="height: 320px; display: flex; flex-direction: column;">
        <div class="controlBoxHead">
        <h3 style="float: left; margin-left: 20px">Stastistics</h3>
        <img src="../assets/icon/option.png" class="optionBtn" >
        </div>
        <div style="display: flex; flex-direction: row; justify-content: space-around;" >
          <div style="height: 250px; border-right: 2px solid rgb(199, 198, 198);">
            <p style="margin-bottom: -20px;">Visitors this week</p>
            <div class='lineChart' id="myLineChart"></div>
          </div>
          <div style="height: 200px">
            <p style="margin-bottom: -20px;">Top visitors</p>
            <div class='barChart' id="myBarChart" ></div>
          </div>
        </div>
      </el-row>
    </el-col>
    <el-col class="shadedbox" :span="8" style="height: 600px; display: flex; flex-direction: column;">
      <div class="controlBoxHead">
        <h3 style="float: left; margin-left: 20px">Control Panel</h3>
        <!-- <img src="../assets/icon/option.png" class="optionBtn" > -->
      </div>
      <div class="controlBoxHead">
        <p style="float: left; margin-left: 10px;">Select Camera</p>
      </div>
      <div class="controlBoxForm">
          <el-form :inline="true" :model="formInline" class="demo-form-inline" style="margin: 15px">
            <el-form-item label="Location">
              <el-input v-model="formInline.user" placeholder="Locate at" />
            </el-form-item>
            <el-form-item label="Camera">
              <el-select v-model="formInline.region" placeholder="Select">
                <el-option label="Zone one" value="shanghai" />
                <el-option label="Zone two" value="beijing" />
              </el-select>
            </el-form-item>
            <el-form-item>
              <div style=" display: flex; flex-direction: row;">
                <el-button type="primary" @click="onSubmit">Query</el-button>
                <el-button type="success" style=" margin-left: 11px" plain>Remote Access</el-button>
                <el-button type="warning" style=" margin-left: 11px" plain>Reboot</el-button>
              </div>
            </el-form-item>
          </el-form>
      </div>
      <div class="controlBoxHead">
        <p style="margin-left: 10px; float: left">Personel List</p>
        <el-popover
          placement="bottom"
          title="Edit"
          :width="100"
          trigger="click"
        >
          <div style=" display: flex; flex-direction: column;">
            <p @click="listMode='add'">Add</p>
            <p @click="listMode='delete'">Delete</p>
          </div>
          <template #reference>
            <img src="../assets/icon/option.png" ref="buttonRef" class="optionBtn" @click="getRecordData">
          </template>
        </el-popover>
      </div>
      <el-scrollbar v-if="listMode!='add'" :style="{'height':scrollBarHeight}" style="margin-top: 5px;">
        <div v-for="visit in recentVisits" :key="visit._id"  class="scrollbar-item-container">
          <div class="scrollbar-demo-item">
            Visitor: {{ visit.visitor?.name }}, Visit Date: {{ visit.date }}
            <el-button v-if="listMode=='delete'" @click="deleteRecord(visit._id)" type="danger" size="small" style="height:23px;width:20px;" plain>-</el-button>  
          </div>
        </div>
      </el-scrollbar>
      <el-button v-if="listMode=='delete'" type="info" plain @click="listMode='normal'" style="margin:10px">Cancel</el-button>
      <el-form :inline="true" :model="addData" class="demo-form-inline" v-if="listMode=='add'" style="margin: 30px; display: flex; flex-direction: column;">
        <el-form-item label="Name">
          <el-input v-model="addData.name" placeholder="Enter Name" />
        </el-form-item>
        <el-form-item label="Date">
          <el-date-picker
            v-model="addData.date"
            type="date"
            placeholder="Pick a day"
          />
        </el-form-item>
        <el-form-item style="margin-left:40px">
          <el-button type="primary" @click="addRecord">Add</el-button>
          <el-button type="info" plain @click="listMode='normal'">Cancel</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
  </div>
</template>

<script >
  import axios from 'axios';
  import { reactive } from 'vue'
  import * as echarts from 'echarts'
  import {onMounted} from "vue"
  // import { ref } from 'vue'

  const API_BASE ="http://52.1.172.234:3000/api/v1"
  // const dialogFormVisible = ref(true)

  export default {
    props:[
    ],
    components:{
    },
    name: 'UserPage',
    data () {
      return {
        formInline: reactive({
          user: '',
          region: '',
        }),
        recentVisits: [
        ],
        dialogFormVisible: true,
        visitorList: [
        ],
        topVisitor: {"guest":1},
        visitWeek: [],
        addData: reactive({
          name: '',
          date: "",
          visitor: ''
        }),
        addVisitor: {
          name: '',
        },
        listMode: "normal",
        scrollBarHeight: '270px',
        };
    },
    watch: {
      listMode(newMode,oldMode){
        if (newMode=='delete') {
          this.scrollBarHeight='230px'
        }
        if (oldMode=='delete') {
          this.scrollBarHeight='270px'
        }
      }
    },
    setup() {
      onMounted(() => { 
        axios.get(`${API_BASE}/visitRecords`).then(response => {
          // console.log('response', response);
          let records = response.data
          // let topVisitor = {}
          // create an object to store the counts
          const topVisitor = {};
          // loop through the list and count the occurrences of the attribute values
          for (let i = 0; i < records.length; i++) {
            if (records[i].visitor) {
              const value = records[i].visitor.name;
              topVisitor[value] = topVisitor[value] ? topVisitor[value] + 1 : 1;
            }
          }
          // console.log(count)

        let myChart = echarts.init(document.getElementById("myLineChart"));
        // 
        myChart.setOption({
          xAxis: {
            data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            axisLabel: {
          rotate: 45, // rotate the labels by 45 degrees
          fontSize: 12 // reduce the font size of the labels
        }
          },
          yAxis:{},
          series: [
            {
              name: "visits",
              type: "line",
              data: [8, 15, 31, 13, 15, 22, 11]
            }
          ]
        });
        window.onresize = function () { // 
          myChart.resize();
        };
        let myChart1 = echarts.init(document.getElementById("myBarChart"));
        // 
        // var chart1Data = {kevin: 3, SuperDvD: 36, guest: 12}
        // console.log(this.topVisitor)
        myChart1.setOption({
          xAxis: {
            data: Object.keys(topVisitor),
            axisLabel: {
          rotate: 45, // rotate the labels by 45 degrees
          fontSize: 12 // reduce the font size of the labels
        }
          },
          yAxis:{},
          series: [
            {
              name: "Visits",
              type: "bar",
              data: Object.values(topVisitor)
            }
          ]
        });
        window.onresize = function () { // 
          myChart1.resize();
        };
      });
    })
    },
    mounted() {
      this.getVisitorData()
      this.getRecordData()
    },
    computed() {
    },
    methods: {
      sendAlert(str, state) {
      let that = this
      if (!this.hasAlert) {
        this.$message({
          message: str,
          type: state
        });
        this.hasAlert = true
        setTimeout(function () {
          that.hasAlert = false
        }, 1000);
      }

      },
      getVisitorData() {
        axios.get(`${API_BASE}/visitors`).then(response => {
          // console.log('response', response);
          this.visitorList = response.data.reverse()
          this.sendAlert("Getting visitors info....","info")
        })
      },
      getRecordData() {
        axios.get(`${API_BASE}/visitRecords`).then(response => {
          // console.log('response', response);
          this.recentVisits = response.data.reverse()
          // console.log(count)
        })
      },
      addRecord() {
        // console.log(this.addData)
        this.addVisitor.name=this.addData.name
        var visitor = this.visitorList.find(item => item.name === this.addData.name)
        if (visitor){
          this.addData.visitor = visitor._id
          axios.post(`${API_BASE}/visitRecords`, this.addData).then(response => {
            console.log('response', response);
            // this.recentVisits = response.data.reverse()
            this.getRecordData()
            this.sendAlert("Added successfully","success")
          })
        }
        else{
          axios.post(`${API_BASE}/visitors`, this.addVisitor).then(response => {
            // console.log('response', response);
            this.addData.visitor = response.data._id
            this.getVisitorData()
            axios.post(`${API_BASE}/visitRecords`, this.addData).then(response => {
            console.log('response', response);
            // this.recentVisits = response.data.reverse()
            this.getRecordData()
            this.sendAlert("Added successfully","success")
          })
          })
        }
        // console.log(this.addData)
      },
      deleteRecord(visitId) {
        console.log(visitId)
        axios.delete(`${API_BASE}/visitRecords/${visitId}`).then(response => {
          console.log('response', response);
          this.getRecordData()
          this.sendAlert("Deleted successfully","warning")
        })
      },

    }
  }

</script>

<style scoped>
  .shadedbox {
    background-color: white;
    border-radius: 14px;
    border: 2px solid rgb(199, 198, 198);
    box-shadow: 2px 2px 2px 1px rgba(78, 78, 255, 0.2);
    margin: 25px
  }

  .optionBtn {
    float: right;
    height: 30px;
    width: 30px;
    margin: 12px;
    /* border: 1px solid rgb(199, 198, 198); */
    border-radius: 4px;
  }

  .controlBoxItem{
    height: 35px; 
    width: 100%;
    display: flex; 
    justify-content: left;
    align-items: center;
    border-bottom: 2px solid rgb(199, 198, 198);
  }
  .controlBoxHead{
    height: 60px; 
    width: 100%;
    border-bottom: 3px solid rgb(199, 198, 198);
  }
  .controlBoxForm{
    height: 160px; 
    width: 100%;
    border-bottom: 2px solid rgb(199, 198, 198);
  }

  .visitorInfo{
    height: 120px;
    width: 90px;
    margin-top: 40px;
    margin-left: 10px;
  }

  .photo{
    height: 70px;
    width: 70px;
    border-radius:50%;
    border: 2px solid rgb(199, 198, 198);
    margin-bottom: 10px;
  }

  .lineChart{
    height: 250px;
    width: 250px;
  }

  .barChart{
    height: 250px;
    width: 250px;
  }

  .scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 10px;
  height: 30px;
  width: 100%;
  text-align: left;
  margin-left: 10px;
  margin-right: 10px;
  color: var(--el-color-primary);
  }
  .scrollbar-item-container {
    display: flex;
    align-items: center;
    justify-content: left;
    height: 30px;
    border-radius: 4px;
    margin: 7px;
    background: var(--el-color-primary-light-9);
  }
</style>