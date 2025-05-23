# Generated by Django 5.2 on 2025-04-11 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_completo", models.CharField(max_length=200)),
                ("data_nascimento", models.DateField()),
                ("idade", models.IntegerField()),
                ("sexo", models.CharField(max_length=20)),
                ("raca_cor", models.CharField(max_length=50)),
                ("cpf", models.CharField(max_length=14)),
                ("telefone", models.CharField(blank=True, max_length=20)),
                ("whatsapp", models.BooleanField()),
                ("estado_civil", models.CharField(blank=True, max_length=50)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("endereco_principal", models.CharField(max_length=200)),
                ("numero", models.CharField(max_length=20)),
                ("bairro", models.CharField(max_length=100)),
                ("municipio_uf", models.CharField(max_length=100)),
                ("microrregiao", models.CharField(blank=True, max_length=100)),
                ("cep", models.CharField(max_length=20)),
                ("ingressara_no_projeto", models.BooleanField()),
                ("turno", models.CharField(blank=True, max_length=50)),
                ("apadrinhado", models.BooleanField()),
                ("responsavel_nome", models.CharField(blank=True, max_length=200)),
                (
                    "responsavel_data_nascimento",
                    models.DateField(blank=True, null=True),
                ),
                ("responsavel_idade", models.IntegerField(blank=True, null=True)),
                ("responsavel_sexo", models.CharField(blank=True, max_length=20)),
                ("responsavel_raca_cor", models.CharField(blank=True, max_length=50)),
                ("responsavel_cpf", models.CharField(blank=True, max_length=14)),
                ("responsavel_telefone", models.CharField(blank=True, max_length=20)),
                ("responsavel_whatsapp", models.BooleanField(default=False)),
                (
                    "responsavel_estado_civil",
                    models.CharField(blank=True, max_length=50),
                ),
                ("responsavel_email", models.EmailField(blank=True, max_length=254)),
                ("escolaridade", models.CharField(blank=True, max_length=100)),
                ("rede_ensino", models.CharField(blank=True, max_length=50)),
                ("ano_ou_periodo", models.CharField(blank=True, max_length=20)),
                ("turno_escolar", models.CharField(blank=True, max_length=50)),
                ("motivo_nao_estuda", models.TextField(blank=True)),
                ("pretende_estudar", models.BooleanField(null=True)),
                ("situacao_profissional", models.CharField(blank=True, max_length=100)),
                ("profissao", models.CharField(blank=True, max_length=100)),
                ("local_trabalho", models.CharField(blank=True, max_length=100)),
                ("bairro_trabalho", models.CharField(blank=True, max_length=100)),
                (
                    "salario",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("conhece_eca", models.CharField(blank=True, max_length=50)),
                ("nocao_cidadania", models.BooleanField(null=True)),
                ("referencia_familiar", models.CharField(blank=True, max_length=20)),
                ("conhece_conselho", models.CharField(blank=True, max_length=100)),
                ("conhece_foscar", models.CharField(blank=True, max_length=100)),
                ("possui_plano", models.BooleanField(null=True)),
                ("nome_plano", models.CharField(blank=True, max_length=100)),
                ("problema_saude", models.BooleanField(null=True)),
                ("acompanhamento_medico", models.BooleanField(null=True)),
                ("cirurgia", models.BooleanField(null=True)),
                ("problema_atual", models.TextField(blank=True)),
                ("deficiencia_fisica", models.BooleanField(null=True)),
                ("tipo_deficiencia", models.CharField(blank=True, max_length=100)),
                ("desenvolvimento_mental", models.TextField(blank=True)),
                ("onde_procura_saude", models.CharField(blank=True, max_length=100)),
                ("refeicoes_dia", models.IntegerField(blank=True, null=True)),
                ("alimentacao", models.TextField(blank=True)),
                ("participa_grupo", models.TextField(blank=True)),
                ("tipo_casa", models.CharField(blank=True, max_length=100)),
                ("moradia_tipo", models.CharField(blank=True, max_length=100)),
                ("vulnerabilidade", models.TextField(blank=True)),
                ("numero_comodos", models.IntegerField(blank=True, null=True)),
                ("divisorias_crianca_adulto", models.BooleanField(null=True)),
                ("tem_banheiro", models.BooleanField(null=True)),
                ("banheiro_dentro", models.BooleanField(null=True)),
                ("energia_publica", models.BooleanField(null=True)),
                ("agua", models.CharField(blank=True, max_length=100)),
                ("destino_lixo", models.CharField(blank=True, max_length=100)),
                ("destino_esgoto", models.CharField(blank=True, max_length=100)),
                ("bens", models.TextField(blank=True)),
                ("origem_bens", models.CharField(blank=True, max_length=100)),
                ("cadastrado_cadunico", models.BooleanField(null=True)),
                ("bolsa_familia", models.BooleanField(null=True)),
                ("auxilio_moradia", models.BooleanField(null=True)),
                ("recebe_bpc", models.BooleanField(null=True)),
                ("faixa_renda_familiar", models.CharField(blank=True, max_length=100)),
                (
                    "renda_per_capita",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("cpf", models.CharField(max_length=14)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Turma",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("horario", models.CharField(max_length=100)),
                (
                    "professor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="portal.professor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Candidato",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portal.candidato",
                    ),
                ),
                (
                    "turma",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="portal.turma",
                    ),
                ),
            ],
        ),
    ]
