<template>
  <div>
    <fieldset>
<h4>Update Tracker Details</h4>
<form action="/:trackid/:logid/update" method="post">
<!-- tracker name -->
<label for="trak_name">Enter New Tracker Name:</label><br>
<input type="text" id="trakname" name="trakname" :value="tracker.trk_name"><br><br>

<!-- tracker description -->
<label for="trak_desc">Enter New Tracker Description:</label><br>
<input type="text" id="trakdesc" name="trakdesc" :value="tracker.description"><br><br>

<!-- tracker type -->
<label for="trak_type">Enter New Tracker Type:</label><br>
<select id="trak_type" name="trak_type">
<span v-for="x in track_type" :key="x">
<option :value="x.traktypeid" v-if="tracker.trk_type==x.traktypeid" selected="selected">
{{ x.trak_type }}
</option>
</span>
</select>
<br><br>
<label for="settings">If Multiple-Choice Tracker, Enter values separated by commas(,)</label><br>
<textarea name="settings" rows="2" cols="30"></textarea><br>
<br>

<br>
<input class="btn" type="submit" value="Update"><br><br>
</form>

<br><a href="/dashboard"> Back to Dashboard</a>
</fieldset>
</div>
</template>

<script>
export default {
  name: 'Tracker_Upd',
};
</script>

<style>
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
a:link {
color: white;
}
a:visited {
color: white;
}
a:hover {
color: #ffbbb1;
}
a:active {
color: white;
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
fieldset{
  display: block;
  background-color: #ffbbb1;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  border-style: none;
}
  </style>
