<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <zing-grid
          ref="booksTable"
          caption="Books"
          nodata="No books! Why don't you add one?"
          editor-controls
          editor="modal"
          loading
          context-menu
          search
        >
          <zg-data idKey="id">
            <zg-param name="src" value="http://localhost:5000/books"></zg-param>
            <zg-param name="recordPath" value="books"></zg-param>
            <zg-param name="loadByPage"> value="true"></zg-param>
            <zg-param name="searchKey" value="search"></zg-param>
          </zg-data>
          <zg-colgroup>
            <zg-column index="title"></zg-column>
            <zg-column index="author"></zg-column>
            <zg-column index="read" type="boolean"></zg-column>
          </zg-colgroup>
        </zing-grid>
      </div>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line
import ZingGrid from 'zinggrid';

export default {};
</script>
