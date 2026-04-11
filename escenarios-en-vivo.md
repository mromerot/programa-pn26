---
layout: page
title: Escenarios en Vivo
permalink: /escenarios-en-vivo/
---

Espacio de transmisión y demostración en tiempo real de herramientas, tecnologías y experiencias aplicadas a la gestión del riesgo de desastres. Las sesiones tienen una duración de **15 minutos** e incluyen demostraciones interactivas, presentaciones relámpago y rondas de preguntas.

<ul class="nav nav-pills mb-4 mt-3" id="live-tabs" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="tab-jue" data-bs-toggle="pill" data-bs-target="#jue" type="button" role="tab" aria-controls="jue" aria-selected="true">
      Jueves 21 mayo
    </button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="tab-vie" data-bs-toggle="pill" data-bs-target="#vie" type="button" role="tab" aria-controls="vie" aria-selected="false">
      Viernes 22 mayo
    </button>
  </li>
</ul>

<div class="tab-content" id="live-tabs-content">

<!-- JUEVES -->
<div class="tab-pane fade show active" id="jue" role="tabpanel" aria-labelledby="tab-jue">
<div class="table-responsive">
<table class="table table-hover align-middle">
<thead class="table-primary">
<tr><th style="width:110px">Hora</th><th>Sesión</th><th>Presentador/a</th></tr>
</thead>
<tbody>
{% assign breaks_jue = "09:30–09:45,11:00–11:15,12:00–14:00,15:30–15:45" | split: "," %}
{% assign break_labels = "Pausa 09:30 – 09:45,Pausa 11:00 – 11:15,Almuerzo 12:00 – 14:00,Pausa 15:30 – 15:45" | split: "," %}
{% assign break_after_jue = "09:15–09:30,10:45–11:00,11:45–12:00,15:15–15:30" | split: "," %}
{% assign break_labels_jue = "Pausa 09:30 – 09:45,Pausa 11:00 – 11:15,Almuerzo 12:00 – 14:00,Pausa 15:30 – 15:45" | split: "," %}
{% for session in site.data.live_sessions.jueves %}
{% assign sid = "jue-" | append: forloop.index %}
<tr>
  <td><strong>{{ session.hora }}</strong></td>
  <td>
    <a class="text-decoration-none fw-semibold" data-bs-toggle="collapse" href="#{{ sid }}" role="button" aria-expanded="false" aria-controls="{{ sid }}">
      {{ session.titulo }}
    </a>
    <div class="collapse mt-2" id="{{ sid }}">
      <p class="text-muted small mb-0">{{ session.resumen }}</p>
    </div>
  </td>
  <td class="text-nowrap">{{ session.presentador }}</td>
</tr>
{% assign hora = session.hora %}
{% if hora == "09:15–09:30" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Pausa 09:30 – 09:45</td></tr>
{% elsif hora == "10:45–11:00" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Pausa 11:00 – 11:15</td></tr>
{% elsif hora == "11:45–12:00" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Almuerzo 12:00 – 14:00</td></tr>
{% elsif hora == "15:15–15:30" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Pausa 15:30 – 15:45</td></tr>
{% endif %}
{% endfor %}
</tbody>
</table>
</div>
</div>

<!-- VIERNES -->
<div class="tab-pane fade" id="vie" role="tabpanel" aria-labelledby="tab-vie">
<div class="table-responsive">
<table class="table table-hover align-middle">
<thead class="table-primary">
<tr><th style="width:110px">Hora</th><th>Sesión</th><th>Presentador/a</th></tr>
</thead>
<tbody>
{% for session in site.data.live_sessions.viernes %}
{% assign sid = "vie-" | append: forloop.index %}
<tr>
  <td><strong>{{ session.hora }}</strong></td>
  <td>
    <a class="text-decoration-none fw-semibold" data-bs-toggle="collapse" href="#{{ sid }}" role="button" aria-expanded="false" aria-controls="{{ sid }}">
      {{ session.titulo }}
    </a>
    <div class="collapse mt-2" id="{{ sid }}">
      <p class="text-muted small mb-0">{{ session.resumen }}</p>
    </div>
  </td>
  <td class="text-nowrap">{{ session.presentador }}</td>
</tr>
{% assign hora = session.hora %}
{% if hora == "09:15–09:30" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Pausa 09:30 – 09:45</td></tr>
{% elsif hora == "10:45–11:00" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Pausa 11:00 – 11:15</td></tr>
{% elsif hora == "11:45–12:00" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Almuerzo 12:00 – 14:00</td></tr>
{% elsif hora == "15:15–15:30" %}
<tr class="table-light"><td colspan="3" class="text-center text-muted fst-italic py-2">Pausa 15:30 – 15:45</td></tr>
{% endif %}
{% endfor %}
</tbody>
</table>
</div>
</div>

</div>
