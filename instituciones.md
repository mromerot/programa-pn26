---
layout: page
title: Instituciones
permalink: /instituciones/
---

Organizaciones del orden nacional, territorial, internacional y académico que participan en la Plataforma Nacional 2026 como ponentes, expositores en Escenarios en Vivo o con presencia en los stands institucionales.

{% assign tipos = "Gobierno nacional,Gobierno territorial,Humanitaria,Internacional,Academia nacional,Academia internacional,Gremio técnico,Organización técnica" | split: "," %}

{% for tipo in tipos %}
{% assign instituciones_tipo = site.data.instituciones | where: "tipo", tipo %}
{% if instituciones_tipo.size > 0 %}

<h2 class="mt-5 mb-3 h5 text-uppercase text-muted border-bottom pb-2">{{ tipo }}</h2>

<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-3 mb-2">
{% for inst in instituciones_tipo %}
<div class="col">
  <div class="card h-100 border-{{ inst.color | default: 'secondary' }} border-opacity-25">
    <div class="card-body">
      <div class="d-flex align-items-start gap-3 mb-2">
        <span class="badge bg-{{ inst.color | default: 'secondary' }} fs-6 flex-shrink-0">{{ inst.sigla }}</span>
        <h3 class="card-title h6 mb-0">{{ inst.nombre }}</h3>
      </div>
      <p class="card-text small text-muted mb-0">{{ inst.descripcion }}</p>
    </div>
  </div>
</div>
{% endfor %}
</div>

{% endif %}
{% endfor %}
