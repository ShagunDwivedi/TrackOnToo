<template>
  <div>
    {{ msg }}
    <fieldset>
<h4>Add New Log </h4>
<!-- tracker name -->
<span v-if="this.tracktype === 'Numerical'">
<label for="value">Enter Value:</label><br>
<input type="text" id="value" name="value" v-model="values"><br><br>
</span>
<!--{% elif track.trk_type==2 %}-->
<span v-if="this.tracktype === 'Boolean'">
<label> Enter Value:</label><br>
<input type="radio" id="true" name="value" value="Yes" v-model="values">
<label for="Yes">Yes</label><br>
<input type="radio" id="false" name="value" value="No" v-model="values">
<label for="No">No</label><br>
</span>
<!--{% elif track.trk_type==4 %}-->
<span v-if="this.tracktype === 'Time Span'">
<label for="time">Select Time Duration (in hh:mm):</label><br>
<input type="time" id="value" name="value" v-model="values"><br>
</span>
<!-- tracker description -->
<span v-if="this.tracktype === 'Multiple Choice'">
<!--{% elif track.trk_type==3 %}-->
<!-- tracker type -->
<label for="value">Enter Value:</label><br>
<select id="value" name="value" v-model="values">
<!--{% for x in values %}-->
<option v-for="sett in settings" :key="sett" :value="sett">{{ sett }}</option>
<!--{% endfor %}-->
</select>
<br><br>
</span>
<!-- option(for multi-valued tracker) -->
<label for="settings">Note:</label><br>
<input type="text" id="message" name="message" v-model="message">
<br>
<br>
<button class="btn" @click.prevent="submitted">Add</button><br><br>

<br><a @click="pushTrack"> Back to Logs</a>
</fieldset>
  </div>
</template>

<script>
function json(response) {
  return response.json();
}
export default {
  name: 'LogAdd',
  data() {
    return {
      msg: '',
      trackid: localStorage.getItem('id'),
      logtype: localStorage.getItem('logtype'),
      values: '',
      message: '',
      tracktype: '',
      settings: '',
    };
  },
  methods: {
    pushTrack() {
      this.$router.push(`/${this.trackid}`);
    },
    submitted() {
      fetch(`http://127.0.0.1:5000/api/tracker/${this.trackid}/logs`, {
        method: 'post',
        mode: 'cors',
        headers: {
          'Content-type': 'application/json',
          Authorization: localStorage.getItem('access_token'),
        },
        body: JSON.stringify({
          note: this.message,
          value: this.values,
        }),
      })
        .then(json)
        .then((data) => {
          if (data.msg === 'Success') {
            this.pushTrack();
          } else {
            this.msg = data.msg;
          }
        });
    },
  },
  mounted() {
    fetch(`http://127.0.0.1:5000/api/tracker/${this.trackid}`, {
      method: 'get',
      headers: {
        Authorization: localStorage.getItem('access_token'),
      },
    })
      .then(json)
      .then((data) => {
        if (data.msg) {
          this.msg = data.msg;
        } else {
          this.tracktype = data.type;
          this.settings = data.settings;
        }
      });
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
a:hover {
  color:#ffbbb1;
  cursor: pointer;
}
ul {
  list-style-type: none;
  margin: 5px;
  padding: 8px;
  background-color: #FFDAC1;
  overflow: hidden;
  color: black;
  width: 60%
}

li {
  float: left;
  display: block;
  border-right: 1px solid black;
}

li a{
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  cursor: pointer;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  color: white;
}
.btn{
  width: 10%;
  background-color: white;
  cursor: pointer;
  padding: 10px 8px;
  border: none;
  color: #653187;
  margin-left: 5px;
}
.btn:hover{
  background-color: #ffbbb1;
  color: #653187;
}
fieldset{
  display: block;
  background-color: #653187;
  width: 50%;
  color: white;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  border-style: none;
}
  </style>
