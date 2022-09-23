<template>
  <div>
    {{ msg }}
    <a @click="pushDash" style="margin-left: 5px">Back to Dashboard</a>
<h1 style="margin-left: 5px">{{ trackname }}</h1>
<h5 style="margin-left: 5px">Tracker Description: {{ description }}</h5>
<!--{% if loglist|length !=0 %}-->
<!-- eslint-disable-next-line max-len -->
<!-- img src="{{url_for('static', filename='plot.jpg')}}" style="margin-left: 15px" height=35% width=40% --><br>
<!--{% endif %}-->
<button class="btn" @click="addLog">Add New Log</button>
<br>
<br>
<span v-if="loglist">
<img src="../../../backend/static/plot.jpg" height=35% width=40%><br>
<!--{% if loglist|length !=0 %}-->
<ul style="color:white; background-color: #653187">
<li>  &emsp;Last Updated  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</li>
<li>  &emsp;Value  &emsp;&emsp;&emsp;</li>
<li>  &emsp;&emsp;Details  &emsp;</li>
<li style="float:right; border-right: none">&emsp;&emsp;Actions&emsp;</li>
</ul>
<br>
<ul v-for="logged in loglist.slice().reverse()" :key="logged">
<li><a @click="pushNon">{{ logged.timestamp.slice(0,11) }}&emsp;</a></li>
<li><a @click="pushNon">&emsp;{{ logged.value }}&emsp;</a></li>
<li><a @click="pushNon">&emsp;{{ logged.note }}&emsp;</a></li>
<div style="float:right;">
<li><a @click="pushUpd(logged.id)">Update&emsp;</a></li>
<!-- eslint-disable-next-line max-len -->
<li style="float:right; border-right: none"><a @click="pushDel(logged.id)">&emsp;Delete</a></li>
</div>
</ul>
<br>
</span>
<p v-if="!loglist" style="margin-left: 5px">No Logs Yet.</p>

</div>
</template>

<script>
function json(response) {
  return response.json();
}
export default {
  name: 'Tracker',
  data() {
    return {
      msg: '',
      trackid: localStorage.getItem('id'),
      trackname: localStorage.getItem('trackname'),
      description: localStorage.getItem('trackdesc'),
      loglist: '',
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:5000/api/tracker/${this.trackid}/logs`, {
      method: 'get',
      headers: {
        Authorization: localStorage.getItem('access_token'),
      },
    })
      .then(json)
      .then((data) => {
        if (data.status) {
          this.loglist = '';
          this.msg = data.status;
        } else {
          localStorage.setItem('loglist', JSON.stringify(data));
          this.loglist = JSON.parse(localStorage.getItem('loglist'));
        }
      });
  },
  methods: {
    addLog() {
      this.$router.push(`/${this.trackid}/addlog`);
    },
    pushDash() {
      this.$router.push('/dashboard');
    },
    pushUpd(logid) {
      localStorage.setItem('logid', JSON.stringify(logid));
      this.$router.push(`/${this.trackid}/${logid}/updatelog`);
    },
    pushDel(logid) {
      localStorage.setItem('logid', JSON.stringify(logid));
      this.$router.push(`/${this.trackid}/${logid}/deletelog`);
    },
  },
};
</script>

<style scoped>
        body{
    background-color: #ffbbb1;
    background-attachment: fixed;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center center;
    margin-top: 0px;
    margin-left: 0px;
    margin-right: 0px;
    }
    .trkname{
      display: block;
      padding-inline-start: 40px;
      background-color: #653187;
      overflow: hidden;
      margin-top: 0px;
      color: white;
    }
    ul {
  list-style-type: none;
  margin: 5px;
  padding: 8px;
  background-color: #FFDAC1;
  overflow: hidden;
  color: white;
  width: 70%
}
a:hover {
  color:#653187;
  cursor: pointer;
}
li {
  float: left;
  display: block;
  border-right: 1px solid black;
  color: white;
}
img{
  margin-left: 15px;
  float: left;
}
li a{
  display: block;
  text-align: center;
  text-decoration: none;
  cursor: pointer;
  color:black;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  color: white;
}
.btn{
  width: 10%;
  background-color: #653187;
  cursor: pointer;
  padding: 10px 8px;
  border: none;
  color: white;
  margin-left: 5px;
}
.btn:hover{
  background-color: #FFDAC1;
  color: #653187;
}
</style>
