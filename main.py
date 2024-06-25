    if os.path.exists(args.res_dir):
        print(f"Directory '{args.res_dir}' already exists. Skipping creation.")
    else:
        os.makedirs(args.res_dir)
        print(f"Directory '{args.res_dir}' did not exist, so it was created.")
