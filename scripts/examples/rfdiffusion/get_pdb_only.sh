base_dir=data/IL13-VHH_Info/VHH5

python scripts/get_pdb_only.py \
    --design_pdb_dir ${base_dir}/design_H123_0 ${base_dir}/design_H123_1 ${base_dir}/design_H123_2 ${base_dir}/design_H123_3 \
    --output_pdb_dir ${base_dir}/design_pdb_only
