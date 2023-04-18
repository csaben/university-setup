# My Vertical Timeline in Markdown

Here's a custom vertical timeline created using HTML:

```html
<style>
  .timeline {
    position: relative;
    max-width: 1200px;
    list-style-type: none;
  }

  .timeline::before {
    content: '';
    position: absolute;
    width: 6px;
    background-color: #6f42c1;
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -3px;
  }

  .timeline-item {
    padding: 10px 40px;
    position: relative;
    background-color: inherit;
    width: 50%;
  }

  .timeline-item::before {
    content: '';
    position: absolute;
    width: 25px;
    height: 25px;
    right: -17px;
    background-color: white;
    border: 4px solid #6f42c1;
    top: 15px;
    border-radius: 50%;
    z-index: 1;
  }

  .left {
    left: 0;
  }

  .right {
    left: 50%;
  }
</style>

<ul class="timeline">
  <li class="timeline-item left">
    <p><strong>2020</strong> - Event description</p>
  </li>
  <li class="timeline-item right">
    <p><strong>2021</strong> - Event description</p>
  </li>
  <li class="timeline-item left">
    <p><strong>2022</strong> - Event description</p>
  </li>
  <!-- Add more timeline items as needed -->
</ul>

